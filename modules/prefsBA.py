# Form implementation generated from reading ui file '/home/phil/kodos/modules/prefsBA.ui'
#
# Created: Mon Apr 28 21:10:53 2003
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
        PrefsBALayout = QVBoxLayout(self)
        PrefsBALayout.setSpacing(6)
        PrefsBALayout.setMargin(11)

        Layout15 = QGridLayout()
        Layout15.setSpacing(6)
        Layout15.setMargin(0)
        spacer = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout15.addMultiCell(spacer,3,3,2,3)

        self.recentFilesSpinBox = QSpinBox(self,'recentFilesSpinBox')
        self.recentFilesSpinBox.setSizePolicy(QSizePolicy(0,0,self.recentFilesSpinBox.sizePolicy().hasHeightForWidth()))
        self.recentFilesSpinBox.setMaxValue(25)
        self.recentFilesSpinBox.setValue(5)

        Layout15.addWidget(self.recentFilesSpinBox,3,1)

        self.browserButton = QPushButton(self,'browserButton')
        self.browserButton.setSizePolicy(QSizePolicy(0,0,self.browserButton.sizePolicy().hasHeightForWidth()))
        self.browserButton.setText(self.tr('...'))

        Layout15.addWidget(self.browserButton,0,3)

        self.browserEdit = QLineEdit(self,'browserEdit')

        Layout15.addMultiCellWidget(self.browserEdit,0,0,1,2)

        self.emailServerEdit = QLineEdit(self,'emailServerEdit')

        Layout15.addMultiCellWidget(self.emailServerEdit,2,2,1,3)

        self.TextLabel1_2 = QLabel(self,'TextLabel1_2')
        self.TextLabel1_2.setSizePolicy(QSizePolicy(0,1,self.TextLabel1_2.sizePolicy().hasHeightForWidth()))
        self.TextLabel1_2.setText(self.tr('Recent Files:'))

        Layout15.addWidget(self.TextLabel1_2,3,0)

        self.TextLabel1 = QLabel(self,'TextLabel1')
        self.TextLabel1.setSizePolicy(QSizePolicy(0,1,self.TextLabel1.sizePolicy().hasHeightForWidth()))
        self.TextLabel1.setText(self.tr('Web Browser:'))

        Layout15.addWidget(self.TextLabel1,0,0)

        self.fontButton = QPushButton(self,'fontButton')
        self.fontButton.setText(self.tr(''))

        Layout15.addMultiCellWidget(self.fontButton,1,1,1,3)

        self.TextLabel1_2Emaii = QLabel(self,'TextLabel1_2Emaii')
        self.TextLabel1_2Emaii.setSizePolicy(QSizePolicy(0,1,self.TextLabel1_2Emaii.sizePolicy().hasHeightForWidth()))
        self.TextLabel1_2Emaii.setText(self.tr('Email Server:'))

        Layout15.addWidget(self.TextLabel1_2Emaii,2,0)

        self.TextLabel2 = QLabel(self,'TextLabel2')
        self.TextLabel2.setSizePolicy(QSizePolicy(0,1,self.TextLabel2.sizePolicy().hasHeightForWidth()))
        self.TextLabel2.setText(self.tr('Editor Font:'))

        Layout15.addWidget(self.TextLabel2,1,0)
        PrefsBALayout.addLayout(Layout15)
        spacer_2 = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        PrefsBALayout.addItem(spacer_2)

        Layout1 = QHBoxLayout()
        Layout1.setSpacing(6)
        Layout1.setMargin(0)

        self.buttonHelp = QPushButton(self,'buttonHelp')
        self.buttonHelp.setText(self.tr('&Help'))
        self.buttonHelp.setAutoDefault(1)
        Layout1.addWidget(self.buttonHelp)
        spacer_3 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(spacer_3)

        self.buttonApply = QPushButton(self,'buttonApply')
        self.buttonApply.setText(self.tr('&Apply'))
        self.buttonApply.setAutoDefault(1)
        Layout1.addWidget(self.buttonApply)

        self.buttonOk = QPushButton(self,'buttonOk')
        self.buttonOk.setText(self.tr('&OK'))
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        Layout1.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(self,'buttonCancel')
        self.buttonCancel.setText(self.tr('&Cancel'))
        self.buttonCancel.setAutoDefault(1)
        Layout1.addWidget(self.buttonCancel)
        PrefsBALayout.addLayout(Layout1)

        self.connect(self.buttonOk,SIGNAL('clicked()'),self,SLOT('accept()'))
        self.connect(self.buttonCancel,SIGNAL('clicked()'),self,SLOT('reject()'))
        self.connect(self.browserButton,SIGNAL('pressed()'),self.browser_slot)
        self.connect(self.fontButton,SIGNAL('pressed()'),self.font_slot)
        self.connect(self.buttonHelp,SIGNAL('pressed()'),self.help_slot)
        self.connect(self.buttonApply,SIGNAL('pressed()'),self.apply_slot)

        self.setTabOrder(self.browserEdit,self.browserButton)
        self.setTabOrder(self.browserButton,self.fontButton)
        self.setTabOrder(self.fontButton,self.emailServerEdit)
        self.setTabOrder(self.emailServerEdit,self.recentFilesSpinBox)
        self.setTabOrder(self.recentFilesSpinBox,self.buttonHelp)
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
