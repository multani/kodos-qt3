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
import modules.xpm as xpm
import sys
import os
import string
import re
import copy
import cPickle
import types

# match status
MATCH_NA = 0
MATCH_OK = 1
MATCH_FAIL = 2

TRUE = 1
FALSE = 0

# regex to find special flags which must begin at beginning of line or after some spaces
EMBEDDED_FLAGS = r"^ *\(\?(?P<flags>[iLmsux]*)\)"

########################################################################################
#
# The Kodos class which defines the main functionality and user interaction
#
########################################################################################

class Kodos(KodosBA):
    def __init__(self, parent):
        self.parent = parent
        KodosBA.__init__(self, parent)
        self.regex = ""
        self.matchstring = ""
        self.flags = 0
        self.createTooltips()
        self.filename = ""
        self.match_num = 0
        self.embedded_flags_obj = re.compile(EMBEDDED_FLAGS)
        self.embedded_flags = ""
        self.regex_embedded_flags_removed = ""

        
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
        #code += "rawstr = r\"\"\"" + self.regex + "\"\"\"\n"
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


    def populate_match_textbrowser(self, startpos, endpos):
        #startpos = span_tuple[0]
        #endpos = span_tuple[1]
        
        # highlight the matching section
        s = "<font color=blue size=+2><b>" + self.matchstring[startpos:endpos] + "</b></font>"

        # prepend the beginning that didn't match
        if startpos > 0:
            s = self.matchstring[0:startpos] + s

        # append the end that didn't match
        if endpos < len(self.matchstring):
            #print endpos, len(self.matchstring), self.matchstring[endpos]
            s += self.matchstring[endpos:]

        # replace newlines w/ <br>'s
        s = string.replace(s, "\n", "<br>")

        # replace spaces w/ nbsp; except in the font tag that we inserted above
        # a better way might be to use an re.sub w/ a function, but this will
        # suffice
        raw = r'(.*)(<font.*>)(.*)'
        matchobj = re.search(raw, s)
        if matchobj:
            pre = matchobj.group(1)
            font = matchobj.group(2)
            post = matchobj.group(3)
            s = ""
            if pre:
                s += string.replace(pre, " ", "&nbsp;")
                
            s += font
            if post:
                s += string.replace(post, " ", "&nbsp;")

        #print s + "\n"
        self.matchTextBrowser.setText(s)


    def clear_results(self):
        self.groupListView.clear()
        self.codeTextBrowser.setText("")
        self.matchTextBrowser.setText("")
        

    def process_regex(self):
        if not self.regex or not self.matchstring:
            self.update_results("Enter a regular expression and a string to match against", MATCH_NA)
            self.clear_results()
            return

        self.process_embedded_flags(self.regex)

        try:
            compile_obj = re.compile(self.regex, self.flags)
            allmatches = compile_obj.findall(self.matchstring)
            if allmatches and len(allmatches):
                self.matchNumberSpinBox.setMaxValue(len(allmatches) - 1)
                self.matchNumberSpinBox.setEnabled(TRUE)
            else:
                self.matchNumberSpinBox.setEnabled(FALSE)
            match_obj = compile_obj.search(self.matchstring)
        except Exception, e:
            self.update_results(str(e), MATCH_FAIL)
            return

            
        if not match_obj:
            self.update_results("Pattern does not match", MATCH_FAIL)
            self.clear_results()
            return

        if self.match_num > 0:
            for i in range(self.match_num):
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

            #print "group_nums:", group_nums                         
            #print "grp index: ", compile_obj.groupindex
            #print "groups:", match_obj.groups()
            #print "span: ", match_obj.span()

            group_tuples = []
            # create group_tuple in the form: (group #, group name, group matches)
            g = allmatches[self.match_num]
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
        

    def openFileDialog(self):
        fn = QFileDialog.getOpenFileName(self.filename, "*.kds\nAll (*)",
                                         self, "Open Kodos File")

        if not fn.isEmpty():
            filename = str(fn)
            self.openFile(filename)


    def openFile(self, filename):
        try:
            fp = open(filename, "r")
        except:
            msg = "Could not open file for reading: " + filename
            self.parent.updateStatus(msg, -1, 5, TRUE)
            return None

        try:
            u = cPickle.Unpickler(fp)
            self.regex = u.load()
            self.regexMultiLineEdit.setText(self.regex)

            self.matchstring = u.load()
            self.stringMultiLineEdit.setText(self.matchstring)
            
            flags = u.load()
            self.set_flags(flags)

            self.filename = filename
            msg = filename + " loaded successfully"
            self.parent.updateStatus(msg, -1, 5, TRUE)
        except Exception, e:
            print str(e)
            msg = "Error reading from file: " + filename
            self.parent.updateStatus(msg, -1, 5, TRUE)


    def saveFileAsDialog(self):
        self.filedialog = QFileDialog(self.filename, "*.kds\nAll (*)", self, "Save Kodos File", TRUE)
        self.filedialog.setCaption("Save Kodos File")
        self.filedialog.show()

        selected = self.filedialog.selectedFile()
        if selected.isEmpty():
            self.parent.updateStatus("No file selected to save", -1, 5, TRUE)
            return
                
        filename = str(self.filedialog.selectedFile())
        if not filename:
            self.parent.updateStatus("No file selected to save", -1, 5, TRUE)
            return
 
        if filename.find(".") == -1:
            filename += ".kds"

        self.filename = filename
        self.saveFile()


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
    def __init__(self):
        QMainWindow.__init__(self, None, None,
                             Qt.WDestructiveClose | Qt.WType_TopLevel)
        self.setGeometry(0, 20, 695, 625)
        self.setCaption("Kodos")

        self.setIcon(getPixmap("kodos_icon.png", "PNG"))

        self.kodos = Kodos(self)
        
        self.createMenuBar()
        self.createStatusBar()
        self.createToolBar()
        
        self.updateStatus("Enter a regular expression and a string to match against", MATCH_NA)

        self.connect(self, PYSIGNAL('copySymbol()'), self.kodos.copy_symbol)
        self.setCentralWidget(self.kodos)
        self.kodos.show()
        self.show()
        self.prefs = Preferences(self, 1)


    def updateStatus(self, status_string, status_value, duration=0, replace=FALSE, tooltip=''):
        if status_value == MATCH_NA:
            pixmap = getPixmap("yellow.png", "PNG")
        elif status_value == MATCH_OK:
            pixmap = getPixmap("green.png", "PNG")
        elif status_value == MATCH_FAIL:
            pixmap = getPixmap("red.png", "PNG")
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

        self.bookButton = QToolButton(toolbar, "book")
        self.bookButton.setPixmap(QPixmap(xpm.bookIcon))
        self.bookTip = Tooltip("Regex Reference Guide")
        self.bookTip.addWidget(self.bookButton)
        self.connect(self.bookButton, SIGNAL("clicked()"), self.reference_guide)

        
        # hack to move logo to right
        label = QLabel("", toolbar)
        toolbar.setStretchableWidget(label)

        self.logolabel = QLabel("logo", toolbar)
        pixmap = getPixmap("ssilogo.png", "PNG")
        self.logolabel.setPixmap(pixmap)

        banner = getPixmap("banner.png", "PNG")
        bannerlabel = QLabel("ssi banner", toolbar)
        bannerlabel.setPixmap(banner)
        

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
        self.filemenu.insertItem(QIconSet(QPixmap(xpm.exitIcon)),
                                 "&Quit", qApp, SLOT("quit()"), Qt.CTRL+Qt.Key_Q )
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
                                           "&Python regex help",
                                           self.regex_help)
        self.helpmenu.insertSeparator()
        self.id = self.helpmenu.insertItem(QIconSet(QPixmap(xpm.bookIcon)),
                                           "Regex &Reference guide",
                                           self.reference_guide)
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


    def reference_guide(self):
        self.ref_win = ReferenceWindow(self)
        

#####################################################################################
#
#
#####################################################################################

qApp = QApplication(sys.argv)

kodos = KodosMainWindow()

qApp.setMainWidget(kodos)

qApp.exec_loop()
