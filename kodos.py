#!/usr/bin/env python
#  kodos.py: -*- Python -*-  DESCRIPTIVE TEXT.

import sys
import os
import string
import re
import copy
import cPickle
import types
import getopt
import urllib
import signal
from qt import *

### make sure that this script can find kodos specific modules ###
import os.path
from distutils.sysconfig import get_python_lib

sys.path.insert(0, os.path.join(get_python_lib(), "kodos")) #, "modules"))

###################################################################

from modules.kodosBA import *
from modules.util import getPixmap, kodos_toolbar_logo
from modules.about import *
import modules.help as help
from modules.tooltip import *
from modules.tooltips import *
from modules.status_bar import *
from modules.reference import *
from modules.prefs import *
from modules.webbrowser import launch_browser
from modules.reportBug import reportBugWindow
from modules.version import VERSION
from modules.recent_files import RecentFiles
import modules.xpm as xpm
from modules.urlDialog import URLDialog
from modules.migrate_settings import MigrateSettings

# match status
MATCH_NA       = 0
MATCH_OK       = 1
MATCH_FAIL     = 2
MATCH_PAUSED   = 3
MATCH_EXAMINED = 4

MSG_NA     = "Enter a regular expression and a string to match against"
MSG_PAUSED = "Kodos regex processing is paused.  Click the pause icon to unpause",
MSG_FAIL   = "Pattern does not match"

TRUE  = 1
FALSE = 0

TIMEOUT = 3

# regex to find special flags which must begin at beginning of line
# or after some spaces
EMBEDDED_FLAGS = r"^ *\(\?(?P<flags>[iLmsux]*)\)"

# colors for normal & examination mode
QCOLOR_WHITE  = QColor(Qt.white)     # normal
QCOLOR_YELLOW = QColor(255,255,127)  # examine

QT_VERS = int(QT_VERSION_STR[0])

if QT_VERS < 3:
    print "Qt versions prior to 3.0 are no longer supported"
    sys.exit(0)

try:
    signal.SIGALRM
    HAS_ALARM = 1
except:
    HAS_ALARM = 0



##############################################################################
#
# The Kodos class which defines the main functionality and user interaction
#
##############################################################################

class Kodos(KodosBA):
    def __init__(self, filename, debug):
        KodosBA.__init__(self)
        self.debug = debug
        self.regex = ""
        self.matchstring = ""
        self.replace = ""
        self.flags = 0
        self.is_paused = 0
        self.is_examined = 0
        self.createTooltips()
        self.filename = ""
        self.match_num = 1 # matches are labeled 1..n
        self.replace_num = 0 # replace all
        self.url = None
        self.group_tuples = None
        
        self.embedded_flags_obj = re.compile(EMBEDDED_FLAGS)
        self.embedded_flags = ""
        self.regex_embedded_flags_removed = ""

        self.createStatusBar()
        
        self.statusPixmapsDict = {MATCH_NA: QPixmap(xpm.yellowStatusIcon),
                                  MATCH_OK: QPixmap(xpm.greenStatusIcon),
                                  MATCH_FAIL: QPixmap(xpm.redStatusIcon),
                                  MATCH_PAUSED: QPixmap(xpm.pauseStatusIcon)}

        
        self.updateStatus(MSG_NA, MATCH_NA)

        self.show()
        self.prefs = Preferences(self, 1)
        self.recent_files = RecentFiles(self,
                                        self.prefs.recentFilesSpinBox.value(),
                                        self.debug)

        if QT_VERS > 2:
            self.matchTextBrowser.setTextFormat(QTextEdit.PlainText)

        if filename and self.openFile(filename):
            qApp.processEvents()

        self.connect(self, PYSIGNAL('prefsSaved()'), self.prefsSaved)

        self.connect(self.fileMenu,
                     SIGNAL('activated(int)'),
                     self.fileMenuHandler)
        
        self.connect(self, PYSIGNAL('copySymbol()'), self.copy_symbol)

        self.connect(self, PYSIGNAL('urlImported()'), self.urlImported)

        kodos_toolbar_logo(self.toolBar)
        if self.replace:  self.show_replace_widgets()
        else:             self.hide_replace_widgets()


##    def setToolbarLogo(self):
##        blankButton = self.toolBar.children()[-1]
##        logoButton = self.toolBar.children()[-1]

##        self.toolBar.setStretchableWidget(blankButton)
        
##        blankButton.hide()
##        blankButton.show()

##        logolabel = QLabel("kodos_logo", self.toolBar)
##        logolabel.setPixmap(QPixmap(xpm.kodosTextIcon))


    def createStatusBar(self):
        self.status_bar = Status_Bar(self, FALSE, "")


    def updateStatus(self, status_string, status_value, duration=0, replace=FALSE, tooltip=''):
        pixmap = self.statusPixmapsDict.get(status_value)

        self.status_bar.set_message(status_string, duration, replace, tooltip, pixmap)


    def fileMenuHandler(self, menuid):
        if self.recent_files.isRecentFile(menuid):
            fn = str(self.fileMenu.text(menuid))
            # qt 2.3 seg faults during the removal/addition of menu items
            if QT_VERS > 2: self.recent_files.add(fn)
            self.openFile(fn)

    def prefsSaved(self):
        if self.debug: print "prefsSaved slot"
        self.recent_files.setNumShown(self.prefs.recentFilesSpinBox.value())   
  
        
    def createTooltips(self):
        # we store the actual messages in a seperate module
        # so the code looks cleaner
        create_kodos_tooltips(self)


    def checkbox_slot(self):
        self.flags = 0
        
        if self.ignorecaseCheckBox.isChecked():
            self.flags = self.flags + re.IGNORECASE

        if self.multilineCheckBox.isChecked():
            self.flags = self.flags + re.MULTILINE

        if self.dotallCheckBox.isChecked():
            self.flags = self.flags + re.DOTALL

        if self.verboseCheckBox.isChecked():
            self.flags = self.flags + re.VERBOSE

        if self.localeCheckBox.isChecked():
            self.flags = self.flags + re.LOCALE

        if self.unicodeCheckBox.isChecked():
            self.flags = self.flags + re.UNICODE

        self.process_regex()


    def set_flags(self, flags):
        # from the given integer value of flags, set the checkboxes
        # this is used when loading a saved file
        if flags & re.IGNORECASE:
            self.ignorecaseCheckBox.setChecked(1)
        else:
            self.ignorecaseCheckBox.setChecked(0)

        if flags & re.MULTILINE:
            self.multilineCheckBox.setChecked(1)
        else:
            self.multilineCheckBox.setChecked(0)
            
        if flags & re.DOTALL:
            self.dotallCheckBox.setChecked(1)
        else:
            self.dotallCheckBox.setChecked(0)
            
        if flags & re.VERBOSE:
            self.verboseCheckBox.setChecked(1)
        else:
            self.verboseCheckBox.setChecked(0)

        if flags & re.LOCALE:
            self.localeCheckBox.setChecked(1)
        else:
            self.localeCheckBox.setChecked(0)

        if flags & re.UNICODE:
            self.unicodeCheckBox.setChecked(1)
        else:
            self.unicodeCheckBox.setChecked(0)


    def get_flags_string(self):
        flags_str = ""
        
        if self.ignorecaseCheckBox.isChecked():
            flags_str += ", re.IGNORECASE"

        if self.multilineCheckBox.isChecked():
            flags_str += ", re.MULTILINE"

        if self.dotallCheckBox.isChecked():
            flags_str += ", re.DOTALL"

        if self.verboseCheckBox.isChecked():
            flags_str += ", re.VERBOSE"

        if self.localeCheckBox.isChecked():
            flags_str += ", re.LOCALE"

        if self.unicodeCheckBox.isChecked():
            flags_str += ", re.UNICODE"

        return flags_str


    def get_embedded_flags_string(self):
        flags_str = flags = ""
        
        if self.ignorecaseCheckBox.isChecked():
            flags += "i"

        if self.multilineCheckBox.isChecked():
            flags += "m"

        if self.dotallCheckBox.isChecked():
            flags += "s"

        if self.verboseCheckBox.isChecked():
            flags += "x"

        if self.localeCheckBox.isChecked():
            flags += "L"

        if self.unicodeCheckBox.isChecked():
            flags += "u"

        if flags:
            flags_str = "(?" + flags + ")"

        return flags_str
        

    def pause(self):
        self.is_paused = not self.is_paused
        if self.debug: print "is_paused:", self.is_paused
        
        if self.is_paused:
            self.update_results(MSG_PAUSED, MATCH_PAUSED)
            self.matchNumberSpinBox.setDisabled(1)

        else:
            self.process_regex()
            self.matchNumberSpinBox.setEnabled(1)            


    def examine(self):
        self.is_examined = not self.is_examined
        if self.debug: print "is_examined:", self.is_examined
        
        if self.is_examined:
            color = QCOLOR_YELLOW
            regex = self.regex
            self.regex_saved = self.regex
            length = len(regex)
            found = 0
            for i in range(length, 0,  -1):
                regex = regex[:i]
                self.process_embedded_flags(self.regex)
                try:
                    m = re.search(regex, self.matchstring, self.flags)
                    if m:
                        if self.debug: print "examined regex:", regex
                        self.__refresh_regex_widget(color, regex)
                        self.regexMultiLineEdit.setReadOnly(1)
                        return
                except:
                    pass
                
            self.__refresh_regex_widget(color, "")
        else:
            regex = self.regex_saved
            color = QCOLOR_WHITE
            self.regexMultiLineEdit.setReadOnly(0)
            self.__refresh_regex_widget(color, regex)
            

    def __refresh_regex_widget(self, base_qcolor, regex):
        self.regexMultiLineEdit.setPaletteBackgroundColor(base_qcolor)
        
        self.regexMultiLineEdit.blockSignals(1)
        self.regexMultiLineEdit.clear()
        self.regexMultiLineEdit.blockSignals(0)
        self.regexMultiLineEdit.setText(regex)


    def match_num_slot(self, num):
        self.match_num = num
        self.process_regex()


    def replace_num_slot(self, num):
        self.replace_num = num
        self.process_regex()
        

    def regex_changed_slot(self):
        self.regex = str(self.regexMultiLineEdit.text())
        self.process_regex()


    def string_changed_slot(self):
        self.matchstring = str(self.stringMultiLineEdit.text())
        self.process_regex()


    def hide_replace_widgets(self):
        self.spacerLabel.hide()
        self.replaceLabel.hide()
        self.replaceNumberSpinBox.hide()
        self.replaceTextBrowser.clear()
        self.replaceTextBrowser.setDisabled(TRUE)

    def show_replace_widgets(self):
        self.spacerLabel.show()
        self.replaceLabel.show()
        self.replaceNumberSpinBox.show()
        self.replaceNumberSpinBox.setEnabled(TRUE)
        self.replaceTextBrowser.setEnabled(TRUE)

    def replace_changed_slot(self):
        self.replace = str(self.replaceTextEdit.text())
        self.process_regex()
        if not self.replace:
            self.hide_replace_widgets()
        else:
            self.show_replace_widgets()


    def update_results(self, msg, val):
        self.updateStatus(msg, val)


    def populate_group_listview(self, tuples):
        self.groupListView.clear()

        num_cols = 3
        for t in tuples:
            item = QListViewItem(self.groupListView)
            for col in range(num_cols):
                item.setText(col, str(t[col]))


    def populate_code_textbrowser(self):
        self.codeTextBrowser.setText("")

        code =  "import re\n\n"
        code += "# common variables\n\n"
        code += "rawstr = r\"\"\"" + self.regex_embedded_flags_removed + "\"\"\"\n"
        code += "embedded_rawstr = r\"\"\"" + self.get_embedded_flags_string() + \
                self.regex_embedded_flags_removed + "\"\"\"\n"
        code += 'matchstr = \"\"\"' + self.matchstring + '\"\"\"'
        code += "\n\n"
        code += "# method 1: using a compile object\n"
        code += "compile_obj = re.compile(rawstr"
        if self.flags != 0:
            code += self.get_flags_string()
        code += ")\n"
        code += "match_obj = compile_obj.search(matchstr)\n\n"
        
        code += "# method 2: using search function (w/ external flags)\n"
        code += "match_obj = re.search(rawstr, matchstr"
        if self.flags != 0:
            code += self.get_flags_string()
        code += ")\n\n"

        code += "# method 3: using search function (w/ embedded flags)\n"
        embedded_str = self.get_embedded_flags_string() + self.regex_embedded_flags_removed
        code += "match_obj = re.search(embedded_rawstr, matchstr)\n\n"

        
        if self.group_tuples:
            code += "# Retrieve group(s) from match_obj\n"
            code += "all_groups = match_obj.groups()\n\n"
            code += "# Retrieve group(s) by index\n"
            i = 0
            named_grps = 0
            for grp in self.group_tuples:
                i += 1
                code += "group_%d = match_obj.group(%d)\n" % (i, i)
                if grp[1]: named_grps = 1

            if named_grps:
                code += "\n# Retrieve group(s) by name\n"    
                for grp in self.group_tuples:
                    if grp[1]:
                        code += "%s = match_obj.group('%s')\n" % (grp[1], grp[1])

            code += "\n"

        if self.replace:
            code += "# Replace string\n"
            code += "newstr = compile_obj.subn('%s', %d)\n" % (self.replace,
                                                               self.replace_num)
        

        self.codeTextBrowser.setText(code)


    def colorize_strings(self, strings, widget, cursorOffset=0):
        widget.clear()

        colors = (QColor(Qt.black), QColor(Qt.blue) )
        i = 0
        pos = widget.getCursorPosition()
        for s in strings:
            widget.setColor(colors[i%2])            
            widget.insert(s)
            if i == cursorOffset: pos = widget.getCursorPosition()
            i += 1
            
        widget.setCursorPosition(pos[0], pos[1])
        

    def populate_match_textbrowser(self, startpos, endpos):
        pre = post = match = ""
        
        match = self.matchstring[startpos:endpos]

        # prepend the beginning that didn't match
        if startpos > 0:
            pre = self.matchstring[0:startpos]
            
        # append the end that didn't match
        if endpos < len(self.matchstring):
            post = self.matchstring[endpos:]
            
        strings = [pre, match, post]
        self.colorize_strings(strings, self.matchTextBrowser, 1)


    def populate_replace_textbrowser(self, spans, nummatches):
        self.replaceTextBrowser.clear()
        if not spans: return


        num = self.replaceNumberSpinBox.value()
        if num == 0: num = nummatches
        
        numreplaced = idx = 0
        text = self.matchstring
        strings = []
        for span in spans:
            if span[0] != 0:
                s = text[idx:span[0]]
            else:
                s = ""
                
            idx = span[1]
            numreplaced += 1
            
            strings.append(s)
            strings.append(self.replace)

            if numreplaced >= num:
                strings.append(text[span[1]:])
                break

        self.colorize_strings(strings, self.replaceTextBrowser)

    
    def populate_matchAll_textbrowser(self, spans):
        self.matchAllTextBrowser.clear()
        if not spans: return

        idx = 0
        text = self.matchstring
        strings = []
        for span in spans:
            if span[0] != 0:
                s = text[idx:span[0]]
            else:
                s = ""
                
            idx = span[1]
            strings.append(s)
            strings.append(text[span[0]:span[1]])

        if 0 <= idx <= len(text): 
            strings.append(text[span[1]:])
            
        self.colorize_strings(strings, self.matchAllTextBrowser)

        
    def clear_results(self):
        self.groupListView.clear()
        self.codeTextBrowser.setText("")
        self.matchTextBrowser.setText("")
        self.matchNumberSpinBox.setEnabled(FALSE)
        self.replaceNumberSpinBox.setEnabled(FALSE)
        self.replaceTextBrowser.setText("")
        self.matchAllTextBrowser.setText("")
        self.filename = ""
        

    def process_regex(self):
        def timeout(signum, frame):
            return

        if self.is_paused:
            return
        
        if not self.regex or not self.matchstring:
            self.update_results(MSG_NA, MATCH_NA)
            self.clear_results()
            return

        self.process_embedded_flags(self.regex)
        #print self.resultTabWidget.currentPageIndex()
        
        if HAS_ALARM:
            signal.signal(signal.SIGALRM, timeout)
            signal.alarm(TIMEOUT)

        try:
            compile_obj = re.compile(self.regex, self.flags)
            allmatches = compile_obj.findall(self.matchstring)

            replace_spans = []
            if allmatches and len(allmatches):
                self.matchNumberSpinBox.setMaxValue(len(allmatches))
                self.matchNumberSpinBox.setEnabled(TRUE)
                self.replaceNumberSpinBox.setMaxValue(len(allmatches))
                self.replaceNumberSpinBox.setEnabled(TRUE)
            else:
                self.matchNumberSpinBox.setEnabled(FALSE)
                self.replaceNumberSpinBox.setEnabled(FALSE)

            match_obj = compile_obj.search(self.matchstring)

        except Exception, e:
            self.update_results(str(e), MATCH_FAIL)
            return

        if HAS_ALARM:
            signal.alarm(0)

        if not match_obj:
            self.update_results(MSG_FAIL, MATCH_FAIL)

            self.clear_results()
            return

        # match_index is the list element for match_num.
        # Therefor match_num is for ui display
        # and match_index is for application logic.
        match_index = self.match_num - 1 
        
        if match_index > 0:
            for i in range(match_index):
                match_obj = compile_obj.search(self.matchstring,
                                               match_obj.end())
                
        self.populate_match_textbrowser(match_obj.start(), match_obj.end())

        self.group_tuples = []

        if match_obj.groups():
            #print match_obj.groups()
            s = "<font color=blue>"
            num_groups = len(match_obj.groups())

            group_nums = {}
            if compile_obj.groupindex:
                keys = compile_obj.groupindex.keys()
                for key in keys:
                    group_nums[compile_obj.groupindex[key]] = key

            if self.debug:
                print "group_nums:", group_nums                         
                print "grp index: ", compile_obj.groupindex
                print "groups:", match_obj.groups()
                print "span: ", match_obj.span()

            # create group_tuple in the form: (group #, group name, group matches)
            g = allmatches[match_index]
            if type(g) == types.TupleType:
                for i in range(len(g)):
                    group_tuple = (i+1, group_nums.get(i+1, ""), g[i])
                    self.group_tuples.append(group_tuple)
            else:
                self.group_tuples.append( (1, group_nums.get(1, ""), g) )
                        
            #print group_tuples
            self.populate_group_listview(self.group_tuples)


        if len(allmatches) == 1:
            status = "Pattern matches (found 1 match)"
        else:
            status = "Pattern matches (found %d matches)" % len(allmatches)
            
        self.update_results(status, MATCH_OK)
        self.populate_code_textbrowser()

        spans = self.findAllSpans(compile_obj)
        if self.replace:
            self.populate_replace_textbrowser(spans, len(allmatches))
        self.populate_matchAll_textbrowser(spans)


    def findAllSpans(self, compile_obj):
        spans = []
        
        match_obj = compile_obj.search(self.matchstring)

        last_span = None
        
        while match_obj:
            start = match_obj.start()
            end   = match_obj.end()
            span = (start, end)
            if last_span == span: break
            
            spans.append(span)
            
            last_span = span
            match_obj = compile_obj.search(self.matchstring, end)

        return spans
        
 

    def fileExit(self):
        qApp.quit()


    def fileNew(self):
        self.regexMultiLineEdit.setText("")
        self.stringMultiLineEdit.setText("")
        self.replaceTextEdit.setText("")
        self.set_flags(0)


    def importURL(self):
        self.urldialog = URLDialog(self, self.url)


    def urlImported(self, html, url):
        self.url = url
        self.stringMultiLineEdit.setText(html)
        

    def importFile(self):
        fn = QFileDialog.getOpenFileName(self.filename, "All (*)",
                                         self, "Import File")
        
        if fn.isEmpty():
            self.updateStatus("A file was not selected for import", -1, 5, TRUE)
            return None

        filename = str(fn)
        
        try:
            fp = open(filename, "r")
        except:
            msg = "Could not open file for reading: " + filename
            self.updateStatus(msg, -1, 5, TRUE)
            return None
        
        data = fp.read()
        fp.close()
        self.stringMultiLineEdit.setText(data)

        
    def fileOpen(self):
        fn = QFileDialog.getOpenFileName(self.filename, "*.kds\nAll (*)",
                                         self, "Open Kodos File")

        if not fn.isEmpty():
            filename = str(fn)
            if self.openFile(filename):
                self.recent_files.add(filename)


    def openFile(self, filename):
        self.filename = None

        try:
            fp = open(filename, "r")
        except:
            msg = "Could not open file for reading: " + filename
            self.updateStatus(msg, -1, 5, TRUE)
            return None

        try:
            u = cPickle.Unpickler(fp)
            self.matchNumberSpinBox.setValue(1)
            self.regex = u.load()
            self.regexMultiLineEdit.setText(self.regex)

            self.matchstring = u.load()
            self.stringMultiLineEdit.setText(self.matchstring)
            
            flags = u.load()
            self.set_flags(flags)

            try:
                replace = u.load()
            except:
                # versions prior to 1.7 did not have replace functionality
                # so kds files saved w/ these versions will throw exception
                # here.
                replace = ""
            self.replaceTextEdit.setText(replace)
            
            self.filename = filename
            msg = filename + " loaded successfully"
            self.updateStatus(msg, -1, 5, TRUE)
            return 1
        except Exception, e:
            print str(e)
            msg = "Error reading from file: " + filename
            self.updateStatus(msg, -1, 5, TRUE)
            return 0


    def fileSaveAs(self):
        while 1:
            self.filedialog = QFileDialog(self.filename,
                                          "*.kds\nAll (*)",
                                          self, "Save Kodos File", TRUE)
            self.filedialog.setCaption("Save Kodos File")
            self.filedialog.setMode(QFileDialog.AnyFile)
            #self.filedialog.show()
            ok = self.filedialog.exec_loop()

            selected = self.filedialog.selectedFile()
            if not ok or selected.isEmpty():
                self.updateStatus("No file selected to save", -1, 5, TRUE)
                return

            filename = str(self.filedialog.selectedFile())
            if not filename:
                self.updateStatus("No file selected to save", -1, 5, TRUE)
                return

            if filename.find(".") == -1:
                filename += ".kds"

            if os.access(filename, os.F_OK):
                message = "The file, %s, already exists.\nWould you like to replace it?" % filename
                cancel = QMessageBox.information(None, "Replace file?",
                                                 message, "&Replace",
                                                 "&Cancel")
                if cancel:
                    # allow user to choose another filename
                    continue

            self.filename = filename
            self.fileSave()
            break


    def fileSave(self):
        if not self.filename:
            self.fileSaveAs()
            return

        try:
            fp = open(self.filename, "w")
        except:
            msg = "Could not open file for writing: " + self.filename
            self.updateStatus(msg, -1, 5, TRUE)
            return None

        p = cPickle.Pickler(fp)
        p.dump(self.regex)
        p.dump(self.matchstring)
        p.dump(self.flags)
        p.dump(self.replace)
        
        fp.close()
        msg = self.filename + " successfully saved"
        self.updateStatus(msg, -1, 5, TRUE)
        self.recent_files.add(self.filename)


    def copy_symbol(self, symbol):
        self.regexMultiLineEdit.insert(symbol)


    def process_embedded_flags(self, regex):
        # determine if the regex contains embedded regex flags.
        # if not, return 0 -- inidicating that the regex has no embedded flags
        # if it does, set the appropriate checkboxes on the UI to reflect the flags that are embedded
        #   and return 1 to indicate that the string has embedded flags

        match = self.embedded_flags_obj.match(regex)
        if not match:
            self.embedded_flags = ""
            self.regex_embedded_flags_removed = regex
            return 0

        self.embedded_flags = match.group('flags')
        self.regex_embedded_flags_removed = self.embedded_flags_obj.sub("", regex, 1)
        
        for flag in self.embedded_flags:
            if flag == 'i':
                self.ignorecaseCheckBox.setChecked(1)
            elif flag == 'L':
                self.localeCheckBox.setChecked(1)
            elif flag == 'm':
                self.multilineCheckBox.setChecked(1)
            elif flag == 's':
                self.dotallCheckBox.setChecked(1)
            elif flag == 'u':
                self.unicodeCheckBox.setChecked(1)
            elif flag == 'x':
                self.verboseCheckBox.setChecked(1)

        return 1


    def getWidget(self):
        widget = qApp.focusWidget()
        if (widget == self.regexMultiLineEdit or
            widget == self.stringMultiLineEdit or
            widget == self.replaceTextEdit or
            widget == self.codeTextBrowser):
            return widget
        else:
            return None


    def widgetMethod(self, methodstr, anywidget=0):
        # execute the methodstr of widget only if widget
        # is one of the editable widgets OR if the method
        # may be applied to any widget.
        widget = qApp.focusWidget()
        if anywidget or (
            widget == self.regexMultiLineEdit or
            widget == self.stringMultiLineEdit or
            widget == self.replaceTextEdit or
            widget == self.codeTextBrowser):
            try:
                eval("widget.%s" % methodstr)
            except:
                pass
        

    def editUndo(self):
        self.widgetMethod("undo()")
        
    def editRedo(self):
        self.widgetMethod("redo()")
            
    def editCopy(self):
        self.widgetMethod("copy()", 1)

    def editCut(self):
        self.widgetMethod("cut()")

    def editPaste(self):
        self.widgetMethod("paste()")


    def preferences(self):
        self.prefs.showPrefsDialog()

            
    def setfont(self, font):
        self.regexMultiLineEdit.setFont(font)
        self.stringMultiLineEdit.setFont(font)
        self.replaceTextEdit.setFont(font)


    def getfont(self):
        return self.regexMultiLineEdit.font()


    def helpHelp(self):
        self.helpWindow = help.Help(self, "kodos.html")


    def helpPythonRegex(self):
        self.helpWindow = help.Help(self, "python" + os.sep + "module-re.html", str(self.prefs.browserEdit.text()))
        

    def helpAbout(self):
        self.aboutWindow = About()
        self.aboutWindow.show()


    def kodos_website(self):
        self.launch_browser_wrapper("http://kodos.sourceforge.net")

            
    def check_for_update(self):
        url = "http://sourceforge.net/project/showfiles.php?group_id=43860"
        try:
            fp = urllib.urlopen(url)
        except:
            self.status_bar.set_message("Failed to open url", 5, TRUE)
            return

        lines = fp.readlines()
        html = string.join(lines)

        rawstr = r"""release_id=.*\">.*(kodos-)(?P<version>.*?)</[aA]>"""
        match_obj = re.search(rawstr, html)
        if match_obj:
            latest_version = match_obj.group('version')
            if latest_version == VERSION:
                QMessageBox.information(None, "No Update is Available",
                                        "You are currently using the latest version of Kodos (%s)" % VERSION)
            else:
                #self.status_bar.set_message("A new version of Kodos is available", 5, TRUE)
                
                message =  "There is a newer version of Kodos available.\n\n" + \
                "You are using version: %s.\n" % VERSION + \
                "The latest version is: %s.\n\n" % latest_version + \
                "Press OK to launch browser\n" 

                self.launch_browser_wrapper(url, "Kodos Update Available", message)
        else:
            message = "Unable to get version info from Sourceforge.\n\nPress OK to launch browser"
            self.launch_browser_wrapper(url, "Unknown version available", message)


    def launch_browser_wrapper(self, url, caption=None, message=None):
        browser = str(self.prefs.browserEdit.text())
        if launch_browser(browser, url, caption, message):
            self.status_bar.set_message("Launching web browser", 3, TRUE)
        else:
            self.status_bar.set_message("Cancelled web browser launch", 3, TRUE)


    def reference_guide(self):
        self.ref_win = ReferenceWindow(self)


    def report_bug(self):
        self.bug_report_win = reportBugWindow(self)
        

##############################################################################
#
#
##############################################################################

def usage():
    print "kodos.py [-f filename | --file=filename ] [ -d debug | --debug=debug ] [ -k kodos_dir ]"
    print
    print "  -f filename | --filename=filename  : Load filename on startup"
    print "  -d debug | --debug=debug           : Set debug to this debug level"
    print "  -k kodos_dir                       : Path containing Kodos images & help subdirs"
    print
    sys.exit(0)

filename=None
debug=0
kodos_dir = os.path.join(sys.prefix, "kodos")

args = sys.argv[1:]
try:
    (opts, getopts) = getopt.getopt(args, 'd:f:k:?h',
                                    ["file=", "debug=",
                                     "help"])
except:
    print "\nInvalid command line option detected."
    usage()

for opt, arg in opts:
    if opt in ('-h', '-?', '--help'):
        usage()
    if opt == '-k':
        kodos_dir = arg
    if opt in ('-d', '--debug'):
        try:
            debug = int(arg)
        except:
            print "debug value must be an integer"
            usage()            
    if opt in ('-f', '--file'):
        filename = arg

os.environ['KODOS_DIR'] = kodos_dir

MigrateSettings()

qApp = QApplication(sys.argv)

kodos = Kodos(filename, debug)

qApp.setMainWidget(kodos)

qApp.exec_loop()
