# Form implementation generated from reading ui file '/home/phil/tools/kodos/modules/kodosBA.ui'
#
# Created: Wed Feb 19 01:41:34 2003
#      by: The Python User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *


class KodosBA(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if name == None:
            self.setName('KodosBA')

        self.resize(705,675)
        self.setCaption(self.tr('Form1'))
        KodosBALayout = QGridLayout(self)
        KodosBALayout.setSpacing(6)
        KodosBALayout.setMargin(11)

        self.Line1 = QFrame(self,'Line1')
        self.Line1.setFrameStyle(QFrame.HLine | QFrame.Sunken)

        KodosBALayout.addMultiCellWidget(self.Line1,3,3,0,2)

        self.GroupBox3 = QGroupBox(self,'GroupBox3')
        self.GroupBox3.setTitle(self.tr('Flags'))
        self.GroupBox3.setColumnLayout(0,Qt.Vertical)
        self.GroupBox3.layout().setSpacing(0)
        self.GroupBox3.layout().setMargin(0)
        GroupBox3Layout = QHBoxLayout(self.GroupBox3.layout())
        GroupBox3Layout.setAlignment(Qt.AlignTop)
        GroupBox3Layout.setSpacing(6)
        GroupBox3Layout.setMargin(11)

        self.ignorecaseCheckBox = QCheckBox(self.GroupBox3,'ignorecaseCheckBox')
        self.ignorecaseCheckBox.setText(self.tr('Ignore Case'))
        GroupBox3Layout.addWidget(self.ignorecaseCheckBox)

        self.multilineCheckBox = QCheckBox(self.GroupBox3,'multilineCheckBox')
        self.multilineCheckBox.setText(self.tr('Multi Line'))
        GroupBox3Layout.addWidget(self.multilineCheckBox)

        self.dotallCheckBox = QCheckBox(self.GroupBox3,'dotallCheckBox')
        self.dotallCheckBox.setText(self.tr('Dot All'))
        GroupBox3Layout.addWidget(self.dotallCheckBox)

        self.verboseCheckBox = QCheckBox(self.GroupBox3,'verboseCheckBox')
        self.verboseCheckBox.setText(self.tr('Verbose'))
        GroupBox3Layout.addWidget(self.verboseCheckBox)

        self.localeCheckBox = QCheckBox(self.GroupBox3,'localeCheckBox')
        self.localeCheckBox.setText(self.tr('Locale'))
        GroupBox3Layout.addWidget(self.localeCheckBox)

        self.unicodeCheckBox = QCheckBox(self.GroupBox3,'unicodeCheckBox')
        self.unicodeCheckBox.setText(self.tr('Unicode'))
        GroupBox3Layout.addWidget(self.unicodeCheckBox)

        KodosBALayout.addMultiCellWidget(self.GroupBox3,1,1,0,2)

        self.GroupBox1 = QGroupBox(self,'GroupBox1')
        self.GroupBox1.setTitle(self.tr('Regular Expression'))
        self.GroupBox1.setColumnLayout(0,Qt.Vertical)
        self.GroupBox1.layout().setSpacing(0)
        self.GroupBox1.layout().setMargin(0)
        GroupBox1Layout = QVBoxLayout(self.GroupBox1.layout())
        GroupBox1Layout.setAlignment(Qt.AlignTop)
        GroupBox1Layout.setSpacing(6)
        GroupBox1Layout.setMargin(11)

        self.regexMultiLineEdit = QMultiLineEdit(self.GroupBox1,'regexMultiLineEdit')
        regexMultiLineEdit_font = QFont(self.regexMultiLineEdit.font())
        regexMultiLineEdit_font.setFamily('adobe-helvetica')
        regexMultiLineEdit_font.setPointSize(14)
        self.regexMultiLineEdit.setFont(regexMultiLineEdit_font)
        self.regexMultiLineEdit.setWordWrap(QMultiLineEdit.NoWrap)
        GroupBox1Layout.addWidget(self.regexMultiLineEdit)

        KodosBALayout.addMultiCellWidget(self.GroupBox1,0,0,0,2)

        self.GroupBox2 = QGroupBox(self,'GroupBox2')
        self.GroupBox2.setTitle(self.tr('String'))
        self.GroupBox2.setColumnLayout(0,Qt.Vertical)
        self.GroupBox2.layout().setSpacing(0)
        self.GroupBox2.layout().setMargin(0)
        GroupBox2Layout = QVBoxLayout(self.GroupBox2.layout())
        GroupBox2Layout.setAlignment(Qt.AlignTop)
        GroupBox2Layout.setSpacing(6)
        GroupBox2Layout.setMargin(11)

        self.stringMultiLineEdit = QMultiLineEdit(self.GroupBox2,'stringMultiLineEdit')
        stringMultiLineEdit_font = QFont(self.stringMultiLineEdit.font())
        stringMultiLineEdit_font.setFamily('adobe-helvetica')
        stringMultiLineEdit_font.setPointSize(14)
        self.stringMultiLineEdit.setFont(stringMultiLineEdit_font)
        self.stringMultiLineEdit.setWordWrap(QMultiLineEdit.NoWrap)
        GroupBox2Layout.addWidget(self.stringMultiLineEdit)

        KodosBALayout.addMultiCellWidget(self.GroupBox2,2,2,0,2)

        self.infoTabWidget = QTabWidget(self,'infoTabWidget')

        self.tab = QWidget(self.infoTabWidget,'tab')
        tabLayout = QVBoxLayout(self.tab)
        tabLayout.setSpacing(6)
        tabLayout.setMargin(11)

        self.groupListView = QListView(self.tab,'groupListView')
        self.groupListView.addColumn(self.tr('Group #'))
        self.groupListView.addColumn(self.tr('Group Name'))
        self.groupListView.addColumn(self.tr('Match'))
        self.groupListView.setAllColumnsShowFocus(1)
        self.groupListView.setShowSortIndicator(1)
        tabLayout.addWidget(self.groupListView)
        self.infoTabWidget.insertTab(self.tab,self.tr('Group'))

        self.tab_2 = QWidget(self.infoTabWidget,'tab_2')
        tabLayout_2 = QVBoxLayout(self.tab_2)
        tabLayout_2.setSpacing(6)
        tabLayout_2.setMargin(11)

        self.matchTextBrowser = QTextBrowser(self.tab_2,'matchTextBrowser')
        self.matchTextBrowser.setTextFormat(QTextBrowser.RichText)
        tabLayout_2.addWidget(self.matchTextBrowser)
        self.infoTabWidget.insertTab(self.tab_2,self.tr('Match'))

        self.tab_3 = QWidget(self.infoTabWidget,'tab_3')
        tabLayout_3 = QVBoxLayout(self.tab_3)
        tabLayout_3.setSpacing(6)
        tabLayout_3.setMargin(11)

        self.codeTextBrowser = QTextBrowser(self.tab_3,'codeTextBrowser')
        tabLayout_3.addWidget(self.codeTextBrowser)
        self.infoTabWidget.insertTab(self.tab_3,self.tr('Sample Code'))

        KodosBALayout.addMultiCellWidget(self.infoTabWidget,5,5,0,2)

        Layout4 = QHBoxLayout()
        Layout4.setSpacing(6)
        Layout4.setMargin(0)

        self.TextLabel3 = QLabel(self,'TextLabel3')
        self.TextLabel3.setText(self.tr('Match number:'))
        Layout4.addWidget(self.TextLabel3)

        self.matchNumberSpinBox = QSpinBox(self,'matchNumberSpinBox')
        self.matchNumberSpinBox.setEnabled(0)
        self.matchNumberSpinBox.setSizePolicy(QSizePolicy(0,0,self.matchNumberSpinBox.sizePolicy().hasHeightForWidth()))
        Layout4.addWidget(self.matchNumberSpinBox)

        KodosBALayout.addLayout(Layout4,4,1)
        spacer = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        KodosBALayout.addItem(spacer,4,2)
        spacer_2 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        KodosBALayout.addItem(spacer_2,4,0)

        self.connect(self.regexMultiLineEdit,SIGNAL('textChanged()'),self.regex_changed_slot)
        self.connect(self.stringMultiLineEdit,SIGNAL('textChanged()'),self.string_changed_slot)
        self.connect(self.ignorecaseCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.multilineCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.dotallCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.verboseCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.localeCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.unicodeCheckBox,SIGNAL('toggled(bool)'),self.checkbox_slot)
        self.connect(self.matchNumberSpinBox,SIGNAL('valueChanged(int)'),self.match_num_slot)

        self.setTabOrder(self.regexMultiLineEdit,self.ignorecaseCheckBox)
        self.setTabOrder(self.ignorecaseCheckBox,self.multilineCheckBox)
        self.setTabOrder(self.multilineCheckBox,self.dotallCheckBox)
        self.setTabOrder(self.dotallCheckBox,self.verboseCheckBox)
        self.setTabOrder(self.verboseCheckBox,self.localeCheckBox)
        self.setTabOrder(self.localeCheckBox,self.unicodeCheckBox)
        self.setTabOrder(self.unicodeCheckBox,self.stringMultiLineEdit)
        self.setTabOrder(self.stringMultiLineEdit,self.matchNumberSpinBox)
        self.setTabOrder(self.matchNumberSpinBox,self.infoTabWidget)
        self.setTabOrder(self.infoTabWidget,self.groupListView)

    def event(self,ev):
        ret = QWidget.event(self,ev)

        if ev.type() == QEvent.ApplicationFontChange:
            regexMultiLineEdit_font = QFont(self.regexMultiLineEdit.font())
            regexMultiLineEdit_font.setFamily('adobe-helvetica')
            regexMultiLineEdit_font.setPointSize(14)
            self.regexMultiLineEdit.setFont(regexMultiLineEdit_font)
            stringMultiLineEdit_font = QFont(self.stringMultiLineEdit.font())
            stringMultiLineEdit_font.setFamily('adobe-helvetica')
            stringMultiLineEdit_font.setPointSize(14)
            self.stringMultiLineEdit.setFont(stringMultiLineEdit_font)

        return ret

    def regex_changed_slot(self):
        print 'KodosBA.regex_changed_slot(): not implemented yet'

    def string_changed_slot(self):
        print 'KodosBA.string_changed_slot(): not implemented yet'

    def checkbox_slot(self):
        print 'KodosBA.checkbox_slot(): not implemented yet'

    def match_num_slot(self):
        print 'KodosBA.match_num_slot(): not implemented yet'
