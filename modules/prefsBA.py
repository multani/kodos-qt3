# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/phil/work/kodos/modules/prefsBA.ui'
#
# Created: Sun Feb 22 17:17:21 2004
#      by: The PyQt User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *

image0_data = [
"32 32 16 1",
". c None",
"# c #000000",
"h c #00009c",
"i c #0000ff",
"c c #005500",
"k c #0065ff",
"m c #31ffff",
"g c #414441",
"j c #525552",
"b c #62ce31",
"e c #9c0000",
"n c #9c65cd",
"l c #a4a1a4",
"a c #cdceff",
"d c #ffff62",
"f c #ffffff",
"...........###########..........",
".........##aaaaaaaaaaa##........",
"........#aaaaa######aaaa#.......",
".......#aaaa##bccbbc##aaa#......",
"......#aaaa#bcbbbbcbcb#aaa#.....",
"......#aaaa#cbbbbbbbbc#aaa#.....",
"......#aaaa#b########b#aaa#.....",
".....#aaaa#b#bbbbbbbb#b#aaa#....",
".....#aaaaa#bb######bb#aaaa#....",
".....#aaaa#bb#dddddd#bb#aaa#....",
".....#aa#a#b#dddddddd#b#a#a#....",
".....#aa###b#dddedddd#b###a#....",
".....#aa#b#b#dddedddd#b#b#a#....",
".....#aaa#bbb#dddddd#bbb#aa#....",
".....#aaaa##bb######bb##aaa#....",
".....#aaaaa#bbbbbbbbbb#aaaa#....",
"......#aaaa##bb####bbb#aaa#.....",
"......#aaaa#bbbbbbbbbb#aaa#.....",
"......#aaaa###bbbbbb###aaa#.....",
"......#aaa#bbb#bbbbbbbb#aa#.....",
"##....#aaa#b#bbbbbb##b#aaa#.....",
"#b#...#aaa##f#bbb##f#b#aaa#.....",
"#bb#...#aaa#gf###fghib#aa#....##",
"#bbb#..#aaa#ihfjfgiikb#aa#...#b#",
".#bbb#.#aaa#kihlg#kmk#aaa#...#b#",
"..#bb#.#aa##mm###biim#aaa#..#bb#",
"..#bb#####bbikbbbbimi#aaa#..#bb#",
"..###bbbbb#bbk###bikbb#aa#..#bb#",
"..#bbbb#bb#bbbbbbbbbbbb##...#bb#",
"..#bb###bb#############nn###bbb#",
".#bb#.#bb#nnnnnnnnnnnnnnn#bbbb#.",
".###..########################.."
]

class PrefsBA(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap(image0_data)

        if not name:
            self.setName("PrefsBA")

        self.setIcon(self.image0)
        self.setSizeGripEnabled(0)

        PrefsBALayout = QVBoxLayout(self,11,6,"PrefsBALayout")

        Layout15 = QGridLayout(None,1,1,0,6,"Layout15")
        spacer = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout15.addMultiCell(spacer,3,3,2,3)

        self.recentFilesSpinBox = QSpinBox(self,"recentFilesSpinBox")
        self.recentFilesSpinBox.setSizePolicy(QSizePolicy(0,0,0,0,self.recentFilesSpinBox.sizePolicy().hasHeightForWidth()))
        self.recentFilesSpinBox.setMaxValue(25)
        self.recentFilesSpinBox.setValue(5)

        Layout15.addWidget(self.recentFilesSpinBox,3,1)

        self.browserButton = QPushButton(self,"browserButton")
        self.browserButton.setSizePolicy(QSizePolicy(0,0,0,0,self.browserButton.sizePolicy().hasHeightForWidth()))

        Layout15.addWidget(self.browserButton,0,3)

        self.browserEdit = QLineEdit(self,"browserEdit")

        Layout15.addMultiCellWidget(self.browserEdit,0,0,1,2)

        self.emailServerEdit = QLineEdit(self,"emailServerEdit")

        Layout15.addMultiCellWidget(self.emailServerEdit,2,2,1,3)

        self.TextLabel1_2 = QLabel(self,"TextLabel1_2")
        self.TextLabel1_2.setSizePolicy(QSizePolicy(0,1,0,0,self.TextLabel1_2.sizePolicy().hasHeightForWidth()))

        Layout15.addWidget(self.TextLabel1_2,3,0)

        self.TextLabel1 = QLabel(self,"TextLabel1")
        self.TextLabel1.setSizePolicy(QSizePolicy(0,1,0,0,self.TextLabel1.sizePolicy().hasHeightForWidth()))

        Layout15.addWidget(self.TextLabel1,0,0)

        self.fontButton = QPushButton(self,"fontButton")

        Layout15.addMultiCellWidget(self.fontButton,1,1,1,3)

        self.TextLabel1_2Emaii = QLabel(self,"TextLabel1_2Emaii")
        self.TextLabel1_2Emaii.setSizePolicy(QSizePolicy(0,1,0,0,self.TextLabel1_2Emaii.sizePolicy().hasHeightForWidth()))

        Layout15.addWidget(self.TextLabel1_2Emaii,2,0)

        self.TextLabel2 = QLabel(self,"TextLabel2")
        self.TextLabel2.setSizePolicy(QSizePolicy(0,1,0,0,self.TextLabel2.sizePolicy().hasHeightForWidth()))

        Layout15.addWidget(self.TextLabel2,1,0)
        PrefsBALayout.addLayout(Layout15)
        spacer_2 = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        PrefsBALayout.addItem(spacer_2)

        Layout1 = QHBoxLayout(None,0,6,"Layout1")

        self.buttonHelp = QPushButton(self,"buttonHelp")
        self.buttonHelp.setAutoDefault(1)
        Layout1.addWidget(self.buttonHelp)
        spacer_3 = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Layout1.addItem(spacer_3)

        self.buttonApply = QPushButton(self,"buttonApply")
        self.buttonApply.setAutoDefault(1)
        Layout1.addWidget(self.buttonApply)

        self.buttonOk = QPushButton(self,"buttonOk")
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)
        Layout1.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(self,"buttonCancel")
        self.buttonCancel.setAutoDefault(1)
        Layout1.addWidget(self.buttonCancel)
        PrefsBALayout.addLayout(Layout1)

        self.languageChange()

        self.resize(QSize(540,260).expandedTo(self.minimumSizeHint()))
        try:
            self.clearWState(Qt.WState_Polished)
        except AttributeError:
            pass


        self.connect(self.buttonOk,SIGNAL("clicked()"),self,SLOT("accept()"))
        self.connect(self.buttonCancel,SIGNAL("clicked()"),self,SLOT("reject()"))
        self.connect(self.browserButton,SIGNAL("pressed()"),self.browser_slot)
        self.connect(self.fontButton,SIGNAL("pressed()"),self.font_slot)
        self.connect(self.buttonHelp,SIGNAL("pressed()"),self.help_slot)
        self.connect(self.buttonApply,SIGNAL("pressed()"),self.apply_slot)

        self.setTabOrder(self.browserEdit,self.browserButton)
        self.setTabOrder(self.browserButton,self.fontButton)
        self.setTabOrder(self.fontButton,self.emailServerEdit)
        self.setTabOrder(self.emailServerEdit,self.recentFilesSpinBox)
        self.setTabOrder(self.recentFilesSpinBox,self.buttonHelp)
        self.setTabOrder(self.buttonHelp,self.buttonApply)
        self.setTabOrder(self.buttonApply,self.buttonOk)
        self.setTabOrder(self.buttonOk,self.buttonCancel)


    def languageChange(self):
        self.setCaption(self.__tr("Preferences"))
        self.browserButton.setText(self.__tr("..."))
        self.TextLabel1_2.setText(self.__tr("Recent Files:"))
        self.TextLabel1.setText(self.__tr("Web Browser:"))
        self.fontButton.setText(QString.null)
        self.TextLabel1_2Emaii.setText(self.__tr("Email Server:"))
        self.TextLabel2.setText(self.__tr("Editor Font:"))
        self.buttonHelp.setText(self.__tr("&Help"))
        self.buttonApply.setText(self.__tr("&Apply"))
        self.buttonOk.setText(self.__tr("&OK"))
        self.buttonCancel.setText(self.__tr("&Cancel"))


    def font_slot(self):
        print "PrefsBA.font_slot(): Not implemented yet"

    def help_slot(self):
        print "PrefsBA.help_slot(): Not implemented yet"

    def browser_slot(self):
        print "PrefsBA.browser_slot(): Not implemented yet"

    def apply_slot(self):
        print "PrefsBA.apply_slot(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("PrefsBA",s,c)
