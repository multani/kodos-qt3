# Form implementation generated from reading ui file '/home/phil/tools/kodos/modules/prefsBA.ui'
#
# Created: Thu Apr 17 23:21:55 2003
#      by: The Python User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *


image0_data = [
'32 32 16 1',
'. c None',
'# c #000000',
'h c #00009c',
'i c #0000ff',
'c c #005500',
'k c #0065ff',
'm c #31ffff',
'g c #414441',
'j c #525552',
'b c #62ce31',
'e c #9c0000',
'n c #9c65cd',
'l c #a4a1a4',
'a c #cdceff',
'd c #ffff62',
'f c #ffffff',
'...........###########..........',
'.........##aaaaaaaaaaa##........',
'........#aaaaa######aaaa#.......',
'.......#aaaa##bccbbc##aaa#......',
'......#aaaa#bcbbbbcbcb#aaa#.....',
'......#aaaa#cbbbbbbbbc#aaa#.....',
'......#aaaa#b########b#aaa#.....',
'.....#aaaa#b#bbbbbbbb#b#aaa#....',
'.....#aaaaa#bb######bb#aaaa#....',
'.....#aaaa#bb#dddddd#bb#aaa#....',
'.....#aa#a#b#dddddddd#b#a#a#....',
'.....#aa###b#dddedddd#b###a#....',
'.....#aa#b#b#dddedddd#b#b#a#....',
'.....#aaa#bbb#dddddd#bbb#aa#....',
'.....#aaaa##bb######bb##aaa#....',
'.....#aaaaa#bbbbbbbbbb#aaaa#....',
'......#aaaa##bb####bbb#aaa#.....',
'......#aaaa#bbbbbbbbbb#aaa#.....',
'......#aaaa###bbbbbb###aaa#.....',
'......#aaa#bbb#bbbbbbbb#aa#.....',
'##....#aaa#b#bbbbbb##b#aaa#.....',
'#b#...#aaa##f#bbb##f#b#aaa#.....',
'#bb#...#aaa#gf###fghib#aa#....##',
'#bbb#..#aaa#ihfjfgiikb#aa#...#b#',
'.#bbb#.#aaa#kihlg#kmk#aaa#...#b#',
'..#bb#.#aa##mm###biim#aaa#..#bb#',
'..#bb#####bbikbbbbimi#aaa#..#bb#',
'..###bbbbb#bbk###bikbb#aa#..#bb#',
'..#bbbb#bb#bbbbbbbbbbbb##...#bb#',
'..#bb###bb#############nn###bbb#',
'.#bb#.#bb#nnnnnnnnnnnnnnn#bbbb#.',
'.###..########################..'
]


class PrefsBA(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        image0 = QPixmap(image0_data)

        if name == None:
            self.setName('PrefsBA')

        self.resize(540,260)
        self.setCaption(self.tr('Preferences'))
        self.setIcon(image0)
        self.setSizeGripEnabled(0)

        LayoutWidget = QWidget(self,'Layout1')
        LayoutWidget.setGeometry(QRect(11,215,518,34))
        Layout1 = QHBoxLayout(LayoutWidget)
        Layout1.setSpacing(6)
        Layout1.setMargin(0)

        self.buttonHelp = QPushButton(LayoutWidget,'buttonHelp')
        self.buttonHelp.setText(self.tr('&Help'))
        self.buttonHelp.setAutoDefault(1)
        Layout1.addWidget(self.buttonHelp)
        spacer = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(spacer)

        self.buttonApply = QPushButton(LayoutWidget,'buttonApply')
        self.buttonApply.setText(self.tr('&Apply'))
        self.buttonApply.setAutoDefault(1)
        Layout1.addWidget(self.buttonApply)

        self.buttonOk = QPushButton(LayoutWidget,'buttonOk')
        self.buttonOk.setText(self.tr('&OK'))
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        Layout1.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(LayoutWidget,'buttonCancel')
        self.buttonCancel.setText(self.tr('&Cancel'))
        self.buttonCancel.setAutoDefault(1)
        Layout1.addWidget(self.buttonCancel)

        LayoutWidget_2 = QWidget(self,'Layout11')
        LayoutWidget_2.setGeometry(QRect(10,14,515,135))
        Layout11 = QGridLayout(LayoutWidget_2)
        Layout11.setSpacing(6)
        Layout11.setMargin(0)

        self.browserButton = QPushButton(LayoutWidget_2,'browserButton')
        self.browserButton.setSizePolicy(QSizePolicy(0,0,self.browserButton.sizePolicy().hasHeightForWidth()))
        self.browserButton.setText(self.tr('...'))

        Layout11.addWidget(self.browserButton,0,4)

        self.browserEdit = QLineEdit(LayoutWidget_2,'browserEdit')

        Layout11.addMultiCellWidget(self.browserEdit,0,0,1,3)

        self.timeoutSpinBox = QSpinBox(LayoutWidget_2,'timeoutSpinBox')
        self.timeoutSpinBox.setSizePolicy(QSizePolicy(0,0,self.timeoutSpinBox.sizePolicy().hasHeightForWidth()))
        self.timeoutSpinBox.setMinValue(1)
        self.timeoutSpinBox.setValue(3)

        Layout11.addWidget(self.timeoutSpinBox,3,2)

        self.TextLabel1 = QLabel(LayoutWidget_2,'TextLabel1')
        self.TextLabel1.setText(self.tr('Web Browser:'))

        Layout11.addWidget(self.TextLabel1,0,0)

        self.TextLabel2 = QLabel(LayoutWidget_2,'TextLabel2')
        self.TextLabel2.setText(self.tr('Editor Font:'))

        Layout11.addWidget(self.TextLabel2,1,0)

        self.TextLabel1_2 = QLabel(LayoutWidget_2,'TextLabel1_2')
        self.TextLabel1_2.setText(self.tr('Regex processing timeout: (seconds)'))

        Layout11.addMultiCellWidget(self.TextLabel1_2,3,3,0,1)

        self.emailServerEdit = QLineEdit(LayoutWidget_2,'emailServerEdit')

        Layout11.addMultiCellWidget(self.emailServerEdit,2,2,1,4)

        self.fontButton = QPushButton(LayoutWidget_2,'fontButton')
        self.fontButton.setText(self.tr(''))

        Layout11.addMultiCellWidget(self.fontButton,1,1,1,4)

        self.TextLabel1_2Emaii = QLabel(LayoutWidget_2,'TextLabel1_2Emaii')
        self.TextLabel1_2Emaii.setText(self.tr('Email Server:'))

        Layout11.addWidget(self.TextLabel1_2Emaii,2,0)

        self.connect(self.buttonOk,SIGNAL('clicked()'),self,SLOT('accept()'))
        self.connect(self.buttonCancel,SIGNAL('clicked()'),self,SLOT('reject()'))
        self.connect(self.browserButton,SIGNAL('pressed()'),self.browser_slot)
        self.connect(self.fontButton,SIGNAL('pressed()'),self.font_slot)
        self.connect(self.buttonHelp,SIGNAL('pressed()'),self.help_slot)
        self.connect(self.buttonApply,SIGNAL('pressed()'),self.apply_slot)

        self.setTabOrder(self.browserEdit,self.browserButton)
        self.setTabOrder(self.browserButton,self.fontButton)
        self.setTabOrder(self.fontButton,self.emailServerEdit)
        self.setTabOrder(self.emailServerEdit,self.timeoutSpinBox)
        self.setTabOrder(self.timeoutSpinBox,self.buttonHelp)
        self.setTabOrder(self.buttonHelp,self.buttonApply)
        self.setTabOrder(self.buttonApply,self.buttonOk)
        self.setTabOrder(self.buttonOk,self.buttonCancel)

    def font_slot(self):
        print 'PrefsBA.font_slot(): not implemented yet'

    def help_slot(self):
        print 'PrefsBA.help_slot(): not implemented yet'

    def browser_slot(self):
        print 'PrefsBA.browser_slot(): not implemented yet'

    def apply_slot(self):
        print 'PrefsBA.apply_slot(): not implemented yet'
