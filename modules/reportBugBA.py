# Form implementation generated from reading ui file '/www/kodos/modules/reportBugBA.ui'
#
# Created: Fri Apr 11 10:08:38 2003
#      by: The Python User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *


class reportBugBA(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if name == None:
            self.setName('reportBugBA')

        self.resize(750,645)
        self.setCaption(self.tr('Form1'))
        reportBugBALayout = QGridLayout(self)
        reportBugBALayout.setSpacing(6)
        reportBugBALayout.setMargin(11)

        Layout8 = QHBoxLayout()
        Layout8.setSpacing(6)
        Layout8.setMargin(0)
        spacer = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout8.addItem(spacer)

        self.submitButton = QPushButton(self,'submitButton')
        self.submitButton.setText(self.tr('Submit Bug Report'))
        Layout8.addWidget(self.submitButton)

        self.cancelButton = QPushButton(self,'cancelButton')
        self.cancelButton.setText(self.tr('Cancel'))
        Layout8.addWidget(self.cancelButton)

        reportBugBALayout.addLayout(Layout8,3,0)

        self.GroupBox6 = QGroupBox(self,'GroupBox6')
        self.GroupBox6.setTitle(self.tr('Kodos State Information'))
        self.GroupBox6.setColumnLayout(0,Qt.Vertical)
        self.GroupBox6.layout().setSpacing(0)
        self.GroupBox6.layout().setMargin(0)
        GroupBox6Layout = QGridLayout(self.GroupBox6.layout())
        GroupBox6Layout.setAlignment(Qt.AlignTop)
        GroupBox6Layout.setSpacing(6)
        GroupBox6Layout.setMargin(11)

        Layout10 = QVBoxLayout()
        Layout10.setSpacing(6)
        Layout10.setMargin(0)

        self.TextLabel4 = QLabel(self.GroupBox6,'TextLabel4')
        self.TextLabel4.setText(self.tr('Regular Expression:'))
        Layout10.addWidget(self.TextLabel4)

        self.TextLabel5 = QLabel(self.GroupBox6,'TextLabel5')
        self.TextLabel5.setText(self.tr('Match String:'))
        Layout10.addWidget(self.TextLabel5)

        GroupBox6Layout.addLayout(Layout10,0,0)

        Layout11 = QVBoxLayout()
        Layout11.setSpacing(6)
        Layout11.setMargin(0)

        self.regexMultiLineEdit = QMultiLineEdit(self.GroupBox6,'regexMultiLineEdit')
        self.regexMultiLineEdit.setReadOnly(1)
        Layout11.addWidget(self.regexMultiLineEdit)

        self.stringMultiLineEdit = QMultiLineEdit(self.GroupBox6,'stringMultiLineEdit')
        self.stringMultiLineEdit.setReadOnly(1)
        Layout11.addWidget(self.stringMultiLineEdit)

        GroupBox6Layout.addLayout(Layout11,0,1)

        reportBugBALayout.addWidget(self.GroupBox6,1,0)

        self.GroupBox5 = QGroupBox(self,'GroupBox5')
        self.GroupBox5.setTitle(self.tr('System Information'))
        self.GroupBox5.setColumnLayout(0,Qt.Vertical)
        self.GroupBox5.layout().setSpacing(0)
        self.GroupBox5.layout().setMargin(0)
        GroupBox5Layout = QGridLayout(self.GroupBox5.layout())
        GroupBox5Layout.setAlignment(Qt.AlignTop)
        GroupBox5Layout.setSpacing(6)
        GroupBox5Layout.setMargin(11)

        self.TextLabel1 = QLabel(self.GroupBox5,'TextLabel1')
        self.TextLabel1.setText(self.tr('Operating System:'))

        GroupBox5Layout.addWidget(self.TextLabel1,0,0)

        self.TextLabel3 = QLabel(self.GroupBox5,'TextLabel3')
        self.TextLabel3.setText(self.tr('PyQt Version:'))

        GroupBox5Layout.addWidget(self.TextLabel3,2,0)

        self.TextLabel2 = QLabel(self.GroupBox5,'TextLabel2')
        self.TextLabel2.setText(self.tr('Python Version:'))

        GroupBox5Layout.addWidget(self.TextLabel2,1,0)

        self.OSEdit = QLineEdit(self.GroupBox5,'OSEdit')

        GroupBox5Layout.addWidget(self.OSEdit,0,1)

        self.pythonVersionEdit = QLineEdit(self.GroupBox5,'pythonVersionEdit')

        GroupBox5Layout.addWidget(self.pythonVersionEdit,1,1)

        self.PyQtVersionEdit = QLineEdit(self.GroupBox5,'PyQtVersionEdit')

        GroupBox5Layout.addWidget(self.PyQtVersionEdit,2,1)

        reportBugBALayout.addWidget(self.GroupBox5,0,0)

        self.GroupBox7 = QGroupBox(self,'GroupBox7')
        self.GroupBox7.setTitle(self.tr('Comments'))
        self.GroupBox7.setColumnLayout(0,Qt.Vertical)
        self.GroupBox7.layout().setSpacing(0)
        self.GroupBox7.layout().setMargin(0)
        GroupBox7Layout = QGridLayout(self.GroupBox7.layout())
        GroupBox7Layout.setAlignment(Qt.AlignTop)
        GroupBox7Layout.setSpacing(6)
        GroupBox7Layout.setMargin(11)

        Layout22 = QGridLayout()
        Layout22.setSpacing(6)
        Layout22.setMargin(0)

        self.commentsMultiLineEdit = QMultiLineEdit(self.GroupBox7,'commentsMultiLineEdit')

        Layout22.addWidget(self.commentsMultiLineEdit,1,1)

        self.TextLabel3_2 = QLabel(self.GroupBox7,'TextLabel3_2')
        self.TextLabel3_2.setText(self.tr('Comments:'))

        Layout22.addWidget(self.TextLabel3_2,1,0)

        self.emailAddressEdit = QLineEdit(self.GroupBox7,'emailAddressEdit')

        Layout22.addWidget(self.emailAddressEdit,0,1)

        self.TextLabel2_2 = QLabel(self.GroupBox7,'TextLabel2_2')
        self.TextLabel2_2.setSizePolicy(QSizePolicy(1,0,self.TextLabel2_2.sizePolicy().hasHeightForWidth()))
        self.TextLabel2_2.setText(self.tr('Email address:'))

        Layout22.addWidget(self.TextLabel2_2,0,0)

        GroupBox7Layout.addLayout(Layout22,0,0)

        reportBugBALayout.addWidget(self.GroupBox7,2,0)

        self.connect(self.submitButton,SIGNAL('clicked()'),self.submit_slot)
        self.connect(self.cancelButton,SIGNAL('clicked()'),self.cancel_slot)

        self.setTabOrder(self.OSEdit,self.pythonVersionEdit)
        self.setTabOrder(self.pythonVersionEdit,self.PyQtVersionEdit)
        self.setTabOrder(self.PyQtVersionEdit,self.emailAddressEdit)
        self.setTabOrder(self.emailAddressEdit,self.commentsMultiLineEdit)
        self.setTabOrder(self.commentsMultiLineEdit,self.submitButton)
        self.setTabOrder(self.submitButton,self.cancelButton)
        self.setTabOrder(self.cancelButton,self.regexMultiLineEdit)
        self.setTabOrder(self.regexMultiLineEdit,self.stringMultiLineEdit)

    def cancel_slot(self):
        print 'reportBugBA.cancel_slot(): not implemented yet'

    def submit_slot(self):
        print 'reportBugBA.submit_slot(): not implemented yet'
