#  kodos.py: -*- Python -*-  DESCRIPTIVE TEXT.

from qt import *
from modules.kodosBA import *
from modules.util import getPixmap
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
from modules.migrate_settings import MigrateSettings

# match status
MATCH_NA = 0
MATCH_OK = 1
MATCH_FAIL = 2
MATCH_PAUSED = 3

TRUE = 1
FALSE = 0

TIMEOUT=3

# regex to find special flags which must begin at beginning of line
# or after some spaces
EMBEDDED_FLAGS = r"^ *\(\?(?P<flags>[iLmsux]*)\)"

QT_VERS = int(QT_VERSION_STR[0])

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
    def __init__(self, parent, filename, debug):
        self.parent = parent
        KodosBA.__init__(self, parent)
        self.debug = debug
        self.regex = ""
        self.matchstring = ""
        self.flags = 0
        self.is_paused = 0
        self.createTooltips()
        self.filename = ""
        self.match_num = 1 # matches are labeled 1..n
        self.embedded_flags_obj = re.compile(EMBEDDED_FLAGS)
        self.embedded_flags = ""
        self.regex_embedded_flags_removed = ""
        if QT_VERS > 2:
            self.matchTextBrowser.setTextFormat(QTextEdit.RichText)

        if filename and self.openFile(filename):
            qApp.processEvents()

        
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
            self.update_results("Kodos regex processing is paused.  Click the pause icon to unpause", MATCH_PAUSED)
        else:
            self.process_regex()


    def match_num_slot(self, num):
        self.match_num = num
        self.process_regex()
        

    def regex_changed_slot(self):
        self.regex = str(self.regexMultiLineEdit.text())
        self.process_regex()


    def string_changed_slot(self):
        self.matchstring = str(self.stringMultiLineEdit.text())
        self.process_regex()


    def update_results(self, msg, val):
        self.parent.updateStatus(msg, val)


    def populate_group_listview(self, tuples):
        self.groupListView.clear()

        num_cols = 3
        for t in tuples:
            item = QListViewItem(self.groupListView)
            for col in range(num_cols):
                item.setText(col, str(t[col]))


    def populate_code_textbrowser(self):
        self.codeTextBrowser.setText("")
        code =  "import re\n"
        code += "# common variables\n"
        code += "rawstr = r\"\"\"" + self.regex_embedded_flags_removed + "\"\"\"\n"
        code += "embedded_rawstr = r\"\"\"" + self.get_embedded_flags_string() + \
                self.regex_embedded_flags_removed + "\"\"\"\n"
        code += 'matchstr = \"\"\"' + self.matchstring + '\"\"\"'
        code += "\n"
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

        self.codeTextBrowser.setText(code)


    def format_html(self, s):
        # replace newlines w/ "<BR>" and replace spaces w/ "&nbsp;"
        if QT_VERS == 3:
            # Note: scrollToAnchor doesn't work properly in qt3 wrt
            # the <BR> tag.  Therefor there will be additional whitespace in
            # the match tab display.
            s = string.replace(s, "\n", "&nbsp;<p>")
        else:
            s = string.replace(s, "\n", "&nbsp;<br>")
        s = string.replace(s, " ", "&nbsp;")
        return s

                
    def populate_match_textbrowser(self, startpos, endpos):
        pre = post = match = ""
        
        # highlight the matching section
        match = '<a name="match"><font color=blue size=+2><b>' + \
                self.matchstring[startpos:endpos] + \
                "</b></font>"

        # prepend the beginning that didn't match
        if startpos > 0:
            pre = self.format_html(self.matchstring[0:startpos])
            
        # append the end that didn't match
        if endpos < len(self.matchstring):
            post = self.format_html(self.matchstring[endpos:])

        self.matchTextBrowser.setText(pre + match + post)
        self.matchTextBrowser.scrollToAnchor("match")


    def clear_results(self):
        self.groupListView.clear()
        self.codeTextBrowser.setText("")
        self.matchTextBrowser.setText("")


    def process_regex(self):
        def timeout(signum, frame):
            return

        if self.is_paused:
            return
        
        if not self.regex or not self.matchstring:
            self.update_results("Enter a regular expression and a string to match against", MATCH_NA)
            self.clear_results()
            return
        
        self.process_embedded_flags(self.regex)

        if HAS_ALARM:
            signal.signal(signal.SIGALRM, timeout)
            signal.alarm(TIMEOUT)

        try:
            compile_obj = re.compile(self.regex, self.flags)
            #print "find all"
            allmatches = compile_obj.findall(self.matchstring)
            #print "found all"
            if allmatches and len(allmatches):
                self.matchNumberSpinBox.setMaxValue(len(allmatches))
                self.matchNumberSpinBox.setEnabled(TRUE)
            else:
                self.matchNumberSpinBox.setEnabled(FALSE)

            match_obj = compile_obj.search(self.matchstring)
        except Exception, e:
            self.update_results(str(e), MATCH_FAIL)
            return

        if HAS_ALARM:
            signal.alarm(0)

        if not match_obj:
            self.update_results("Pattern does not match", MATCH_FAIL)
            self.clear_results()
            return

        # match_index is the list element for match_num.
        # Therefor match_num is for ui display
        # and match_index is for application logic.
        match_index = self.match_num - 1 
        
        if match_index > 0:
            for i in range(match_index):
                match_obj = compile_obj.search(self.matchstring, match_obj.end())
                
        self.populate_match_textbrowser(match_obj.start(), match_obj.end())

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

            group_tuples = []
            # create group_tuple in the form: (group #, group name, group matches)
            g = allmatches[match_index]
            if type(g) == types.TupleType:
                for i in range(len(g)):
                    group_tuple = (i+1, group_nums.get(i+1, ""), g[i])
                    group_tuples.append(group_tuple)
            else:
                group_tuples.append( (1, group_nums.get(1, ""), g) )
                        
            #print group_tuples
            self.populate_group_listview(group_tuples)

        if len(allmatches) == 1:
            status = "Pattern matches (found 1 match)"
        else:
            status = "Pattern matches (found %d matches)" % len(allmatches)
            
        self.update_results(status, MATCH_OK)
        self.populate_code_textbrowser()


    def clearAll(self):
        self.regexMultiLineEdit.setText("")
        self.stringMultiLineEdit.setText("")
        self.set_flags(0)


    def importFile(self):
        fn = QFileDialog.getOpenFileName(self.filename, "All (*)",
                                         self, "Import File")
        
        if fn.isEmpty():
            self.parent.updateStatus("A file was not selected for import", -1, 5, TRUE)
            return None

        filename = str(fn)
        
        try:
            fp = open(filename, "r")
        except:
            msg = "Could not open file for reading: " + filename
            self.parent.updateStatus(msg, -1, 5, TRUE)
            return None
        
        data = fp.read()
        fp.close()
        self.stringMultiLineEdit.setText(data)
        

    def openFileDialog(self):
        fn = QFileDialog.getOpenFileName(self.filename, "*.kds\nAll (*)",
                                         self, "Open Kodos File")

        if not fn.isEmpty():
            filename = str(fn)
            if self.openFile(filename):
                self.parent.recent_files.add(filename)


    def openFile(self, filename):
        self.filename = None

        try:
            fp = open(filename, "r")
        except:
            msg = "Could not open file for reading: " + filename
            self.parent.updateStatus(msg, -1, 5, TRUE)
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

            self.filename = filename
            msg = filename + " loaded successfully"
            self.parent.updateStatus(msg, -1, 5, TRUE)
            return 1
        except Exception, e:
            print str(e)
            msg = "Error reading from file: " + filename
            self.parent.updateStatus(msg, -1, 5, TRUE)
            return 0


    def saveFileAsDialog(self):
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
                self.parent.updateStatus("No file selected to save", -1, 5, TRUE)
                return

            filename = str(self.filedialog.selectedFile())
            if not filename:
                self.parent.updateStatus("No file selected to save", -1, 5, TRUE)
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
            self.saveFile()
            break


    def saveFile(self):
        if not self.filename:
            self.saveFileAsDialog()
            return

        try:
            fp = open(self.filename, "w")
        except:
            msg = "Could not open file for writing: " + self.filename
            self.parent.updateStatus(msg, -1, 5, TRUE)
            return None

        p = cPickle.Pickler(fp)
        p.dump(self.regex)
        p.dump(self.matchstring)
        p.dump(self.flags)
        
        fp.close()
        msg = self.filename + " successfully saved"
        self.parent.updateStatus(msg, -1, 5, TRUE)
        self.parent.recent_files.add(self.filename)


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
        
#############################################################################################
#
# The Kodos Main Window which includes the menubar, toolbar, statusbar, etc...
#
############################################################################################
            

class KodosMainWindow(QMainWindow):
    def __init__(self, filename, debug):
        QMainWindow.__init__(self, None, None,
                             Qt.WDestructiveClose | Qt.WType_TopLevel)

        self.debug = debug
        
        self.setGeometry(0, 20, 695, 625)
        self.setCaption("Kodos")

        self.setIcon(getPixmap("kodos_icon.png", "PNG"))

        self.createStatusBar()
        self.updateStatus("Enter a regular expression and a string to match against", MATCH_NA)

        self.kodos = Kodos(self, filename, self.debug)
        
        self.createMenuBar()
        self.createToolBar()
        

        self.connect(self, PYSIGNAL('copySymbol()'), self.kodos.copy_symbol)
        self.setCentralWidget(self.kodos)
        self.kodos.show()
        self.show()
        self.prefs = Preferences(self, 1)
        self.recent_files = RecentFiles(self, self.prefs.recentFilesSpinBox.value(), self.debug)
        self.connect(self, PYSIGNAL('prefsSaved()'), self.prefsSaved)
        self.connect(self.filemenu, SIGNAL('activated(int)'), self.fileMenuHandler)


    def fileMenuHandler(self, menuid):
        if self.recent_files.isRecentFile(menuid):
            fn = str(self.filemenu.text(menuid))
            # qt 2.3 seg faults during the removal/addition of menu items
            if QT_VERS > 2: self.recent_files.add(fn)
            self.kodos.openFile(fn)
            

    def prefsSaved(self):
        if self.debug: print "prefsSaved slot"
        self.recent_files.setNumShown(self.prefs.recentFilesSpinBox.value())
        

    def updateStatus(self, status_string, status_value, duration=0, replace=FALSE, tooltip=''):
        if status_value == MATCH_NA:
            pixmap = getPixmap("yellow.png", "PNG")
        elif status_value == MATCH_OK:
            pixmap = getPixmap("green.png", "PNG")
        elif status_value == MATCH_FAIL:
            pixmap = getPixmap("red.png", "PNG")
        elif status_value == MATCH_PAUSED:
            pixmap = getPixmap("pause.png", "PNG")
        else:
            pixmap = None

        self.status_bar.set_message(status_string, duration, replace, tooltip, pixmap)
                


    def createToolBar(self):
        toolbar = QToolBar(self)
        toolbar.setStretchableWidget(self.menubar)

        self.openPixmap = QPixmap(xpm.openIcon)
        self.openButton = QToolButton(toolbar, "openbutton")
        self.openButton.setPixmap(self.openPixmap)
        self.openTooltip = Tooltip("Open Kodos File")
        self.openTooltip.addWidget(self.openButton)
        self.connect(self.openButton, SIGNAL("clicked()"), self.kodos.openFileDialog)


        self.savePixmap = QPixmap(xpm.saveIcon)
        self.saveButton = QToolButton(toolbar, "savebutton")
        self.saveButton.setPixmap(self.savePixmap)
        self.saveTooltip = Tooltip("Save Kodos File")
        self.saveTooltip.addWidget(self.saveButton)
        self.connect(self.saveButton, SIGNAL("clicked()"), self.kodos.saveFile)

        toolbar.addSeparator()

        self.cutButton = QToolButton(toolbar, "cut")
        self.cutButton.setPixmap(QPixmap(xpm.cutIcon))
        self.cutTip = Tooltip("Cut text")
        self.cutTip.addWidget(self.cutButton)
        self.connect(self.cutButton, SIGNAL("clicked()"), self.cut)

        self.copyButton = QToolButton(toolbar, "copy")
        self.copyButton.setPixmap(QPixmap(xpm.copyIcon))
        self.copyTip = Tooltip("Copy text")
        self.copyTip.addWidget(self.copyButton)
        self.connect(self.copyButton, SIGNAL("clicked()"), self.copy)

        self.pasteButton = QToolButton(toolbar, "paste")
        self.pasteButton.setPixmap(QPixmap(xpm.pasteIcon))
        self.pasteTip = Tooltip("Paste text")
        self.pasteTip.addWidget(self.pasteButton)
        self.connect(self.pasteButton, SIGNAL("clicked()"), self.paste)

        toolbar.addSeparator()

        self.pauseButton = QToolButton(toolbar, "pause")
        self.pauseButton.setPixmap(QPixmap(xpm.pauseIcon))
        self.pauseTip = Tooltip("(un)pause regex processing")
        self.pauseTip.addWidget(self.pauseButton)
        self.connect(self.pauseButton, SIGNAL("clicked()"), self.kodos.pause)

        toolbar.addSeparator()

        self.bookButton = QToolButton(toolbar, "book")
        self.bookButton.setPixmap(QPixmap(xpm.bookIcon))
        self.bookTip = Tooltip("Regex Reference Guide")
        self.bookTip.addWidget(self.bookButton)
        self.connect(self.bookButton, SIGNAL("clicked()"), self.reference_guide)

        self.logolabel = kodos_toolbar_logo(toolbar)
        

    def createStatusBar(self):
        self.status_bar = Status_Bar(self, FALSE, "")


    def createMenuBar(self):
         # create a menubar
        self.menubar = QMenuBar(self)
        self.menubar.setSeparator(1)

        # populate "File" 
        self.filemenu = QPopupMenu()
        self.filemenu.insertItem(QIconSet(QPixmap(xpm.openIcon)),
                                 "&Open", self.kodos.openFileDialog)
        
        self.saveid = self.filemenu.insertItem(QIconSet(QPixmap(xpm.saveIcon)),
                                               "&Save", self.kodos.saveFile)
        self.saveasid = self.filemenu.insertItem("Save As", self.kodos.saveFileAsDialog)
        self.filemenu.insertSeparator()
        self.importid = self.filemenu.insertItem("Import file", self.kodos.importFile)
        self.filemenu.insertSeparator()     
        self.saveasid = self.filemenu.insertItem("Clear All", self.kodos.clearAll)
        self.filemenu.insertSeparator()
        self.filemenu.insertItem(QIconSet(QPixmap(xpm.exitIcon)),
                                 "&Quit", qApp, SLOT("quit()"), Qt.CTRL+Qt.Key_Q )
        self.filemenu.insertSeparator()
        self.menubar.insertItem("&File", self.filemenu)


        self.editmenu = QPopupMenu()
        self.cutid = self.editmenu.insertItem(QIconSet(QPixmap(xpm.cutIcon)),
                                              "Cu&t", self.cut, Qt.CTRL+Qt.Key_X )

        self.copyid = self.editmenu.insertItem(QIconSet(QPixmap(xpm.copyIcon)),
                                               "&Copy", self.copy, Qt.CTRL+Qt.Key_C )

        self.pasteid = self.editmenu.insertItem(QIconSet(QPixmap(xpm.pasteIcon)),
                                                "&Paste", self.paste, Qt.CTRL+Qt.Key_V )
        self.editmenu.insertSeparator()
        self.editmenu.insertItem("P&references", self.preferences)
        self.menubar.insertItem("&Edit", self.editmenu)


        # populate "Help"
        self.helpmenu = QPopupMenu()
        self.id = self.helpmenu.insertItem(QIconSet(QPixmap(xpm.helpIcon)),
                                           "&Help", self.help)
        self.id = self.helpmenu.insertItem(QIconSet(QPixmap(xpm.pythonIcon)),
                                           "&Python Regex Help",
                                           self.regex_help)
        self.helpmenu.insertSeparator()
        self.id = self.helpmenu.insertItem(QIconSet(QPixmap(xpm.bookIcon)),
                                           "&Regex Reference Guide",
                                           self.reference_guide)
        self.helpmenu.insertSeparator()
        self.id = self.helpmenu.insertItem("&Visit the Kodos Website", self.kodos_website)
        self.id = self.helpmenu.insertItem("&Check for Update", self.check_for_update)
        self.id = self.helpmenu.insertItem("Report a &Bug", self.report_bug)
        self.helpmenu.insertSeparator()
        self.id = self.helpmenu.insertItem("&About...", self.about)
        self.menubar.insertItem("&Help", self.helpmenu)       


    def copy(self):
        widget = qApp.focusWidget()
        if (widget == self.kodos.regexMultiLineEdit or
            widget == self.kodos.stringMultiLineEdit or
            widget == self.kodos.codeTextBrowser):
            widget.copy()
            

    def cut(self):
        widget = qApp.focusWidget()
        if (widget == self.kodos.regexMultiLineEdit or
            widget == self.kodos.stringMultiLineEdit):
            widget.cut()        


    def paste(self):
        widget = qApp.focusWidget()
        if (widget == self.kodos.regexMultiLineEdit or
            widget == self.kodos.stringMultiLineEdit):
            widget.paste()        


    def preferences(self):
        self.prefs.showPrefsDialog()

            
    def setfont(self, font):
        self.kodos.regexMultiLineEdit.setFont(font)
        self.kodos.stringMultiLineEdit.setFont(font)


    def getfont(self):
        return self.kodos.regexMultiLineEdit.font()


    def help(self):
        self.helpWindow = help.Help(self, "kodos.html")


    def regex_help(self):
        self.helpWindow = help.Help(self, "python" + os.sep + "module-re.html", str(self.prefs.browserEdit.text()))
        

    def about(self):
        self.aboutWindow = About()
        self.aboutWindow.show()


    def kodos_website(self):
        self.launch_browser_wrapper("http://kodos.sourceforge.net")

            
    def check_for_update(self):
        url = "https://sourceforge.net/project/showfiles.php?group_id=43860"
        try:
            fp = urllib.urlopen(url)
        except:
            self.status_bar.set_message("Failed to open url", 5, TRUE)
            return

        lines = fp.readlines()
        html = string.join(lines)

        rawstr = r"""release_id=.*\">kodos-(?P<version>.*?)<"""
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


    def launch_browser_wrapper(self, url, caption=None, message=None):
        browser = str(self.prefs.browserEdit.text())
        if launch_browser(browser, url, caption, message):
            self.status_bar.set_message("Launching web browser", 3, TRUE)
        else:
            self.status_bar.set_message("Cancelled web browser launch", 3, TRUE)


    def reference_guide(self):
        self.ref_win = ReferenceWindow(self)


    def report_bug(self):
        self.bug_report_win = reportBugWindow(self.kodos)

##############################################################################
#
#
##############################################################################

def usage():
    print "kodos.py [-f filename | --file=filename ] [ -d debug | --debug=debug ]"
    print
    print "  -f filename | --filename=filename  : Load filename on startup"
    print "  -d debug | --debug=debug           : Set debug to this debug level"
    print
    sys.exit(0)

filename=None
debug=0

args = sys.argv[1:]
try:
    (opts, getopts) = getopt.getopt(args, 'd:f:?h',
                                    ["file=", "debug=",
                                     "help"])
except:
    print "\nInvalid command line option detected."
    usage()

for opt, arg in opts:
    if opt in ('-h', '-?', '--help'):
        usage()
    if opt in ('-d', '--debug'):
        try:
            debug = int(arg)
        except:
            print "debug value must be an integer"
            usage()            
    if opt in ('-f', '--file'):
        filename = arg
               
MigrateSettings()

qApp = QApplication(sys.argv)

kodos = KodosMainWindow(filename, debug)

qApp.setMainWidget(kodos)

qApp.exec_loop()
