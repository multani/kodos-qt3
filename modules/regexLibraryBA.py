# Form implementation generated from reading ui file '/home/phil/work/kodos/modules/regexLibraryBA.ui'
#
# Created: Thu Dec 4 20:08:39 2003
#      by: The PyQt User Interface Compiler (pyuic)
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
image1_data = [
"22 22 8 1",
". c None",
"# c #000000",
"e c #000083",
"c c #838100",
"b c #838183",
"d c #c5c2c5",
"a c #ffff00",
"f c #ffffff",
"......................",
".......#####..........",
"..######aaa######.....",
".######aaaaa######....",
"##bcb##a###a##bcb##...",
"#bcb#ddddddddd#bcb#...",
"#cbc#ddddddddd#cbc#...",
"#bcb###########bcb#...",
"#cbcbcbcbcbcbcbcbc#...",
"#bcbcbcbcbcbcbcbcb#...",
"#cbcbcbceeeeeeeeee#...",
"#bcbcbcbefffffffefe...",
"#cbcbcbcefeeeeefeffe..",
"#bcbcbcbefffffffefffe.",
"#cbcbcbcefeeeeefeffffe",
"#bcbcbcbefffffffeeeeee",
"#cbcbcbcefeeeeeffffffe",
"#bcbcbcbeffffffffffffe",
"#cbcbcbcefeeeeeeeeeefe",
".#######effffffffffffe",
"........eeeeeeeeeeeeee",
"......................"
]
image2_data = [
"20 20 20 1",
". c None",
"b c #000000",
"n c #181818",
"q c #202420",
"p c #313031",
"k c #393c39",
"c c #525000",
"a c #626162",
"r c #6a6d6a",
"l c #838100",
"j c #949500",
"# c #b4b6b4",
"i c #bdba00",
"o c #dede00",
"d c #ffaa20",
"e c #ffc66a",
"f c #ffe2b4",
"m c #ffff00",
"h c #ffff6a",
"g c #ffffff",
".#aaaaaaaaaaaaaaaa#.",
"#abbbbbbbbbbbbbbbba#",
"abcdeeeeeeeeeeeedcba",
"abdefffffffffffffdba",
"abefgghijaklihhhfeba",
"abefghmklhabnohhfeba",
"abefghobphobbihhfeba",
"abefghhpahobbihhfeba",
"abefghhhhhlbkohhfeba",
"abefghhhhhqaohhhfeba",
"abefhhhhhrihhhhhfeba",
"abefhhhhokjhhhhhfeba",
"abefhhhhabbhhhhhfeba",
"abefhhhhjbkhhhhhfeba",
"abdehhhhhhhhhhffedba",
"abcdfhffeeeeeeeedcba",
".abbfffedbbbbbbbbba#",
"..abeedbbkaaaaaaaa#.",
"..abdbbka...........",
"..abbba#............"
]

class RegexLibraryBA(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        image0 = QPixmap(image0_data)
        image1 = QPixmap(image1_data)
        image2 = QPixmap(image2_data)

        if not name:
            self.setName("RegexLibraryBA")

        self.setIcon(image0)

        self.setCentralWidget(QWidget(self,"qt_central_widget"))
        RegexLibraryBALayout = QGridLayout(self.centralWidget(),1,1,11,6,"RegexLibraryBALayout")

        self.groupBox5 = QGroupBox(self.centralWidget(),"groupBox5")
        self.groupBox5.setColumnLayout(0,Qt.Vertical)
        self.groupBox5.layout().setSpacing(6)
        self.groupBox5.layout().setMargin(11)
        groupBox5Layout = QGridLayout(self.groupBox5.layout())
        groupBox5Layout.setAlignment(Qt.AlignTop)

        self.descriptionListBox = QListBox(self.groupBox5,"descriptionListBox")

        groupBox5Layout.addWidget(self.descriptionListBox,0,0)

        RegexLibraryBALayout.addWidget(self.groupBox5,0,0)

        self.tabWidget3 = QTabWidget(self.centralWidget(),"tabWidget3")

        self.tab = QWidget(self.tabWidget3,"tab")
        tabLayout = QGridLayout(self.tab,1,1,11,6,"tabLayout")

        self.regexTextBrowser = QTextBrowser(self.tab,"regexTextBrowser")
        self.regexTextBrowser.setTextFormat(QTextBrowser.PlainText)

        tabLayout.addWidget(self.regexTextBrowser,0,0)
        self.tabWidget3.insertTab(self.tab,"")

        self.tab_2 = QWidget(self.tabWidget3,"tab_2")
        tabLayout_2 = QGridLayout(self.tab_2,1,1,11,6,"tabLayout_2")

        self.noteTextBrowser = QTextBrowser(self.tab_2,"noteTextBrowser")
        self.noteTextBrowser.setTextFormat(QTextBrowser.PlainText)

        tabLayout_2.addWidget(self.noteTextBrowser,0,0)

        layout3 = QHBoxLayout(None,0,6,"layout3")

        self.textLabel3 = QLabel(self.tab_2,"textLabel3")
        layout3.addWidget(self.textLabel3)

        self.contribEdit = QLineEdit(self.tab_2,"contribEdit")
        self.contribEdit.setFrameShape(QLineEdit.LineEditPanel)
        self.contribEdit.setFrameShadow(QLineEdit.Sunken)
        self.contribEdit.setReadOnly(1)
        layout3.addWidget(self.contribEdit)

        tabLayout_2.addLayout(layout3,1,0)
        self.tabWidget3.insertTab(self.tab_2,"")

        RegexLibraryBALayout.addWidget(self.tabWidget3,1,0)

        self.editPasteAction = QAction(self,"editPasteAction")
        self.editPasteAction.setIconSet(QIconSet(image1))
        self.helpHelpAction = QAction(self,"helpHelpAction")
        self.helpHelpAction.setIconSet(QIconSet(image2))
        self.exitAction = QAction(self,"exitAction")


        self.toolBar = QToolBar("",self,Qt.DockTop)

        self.editPasteAction.addTo(self.toolBar)


        self.MenuBar = QMenuBar(self,"MenuBar")

        self.fileMenu = QPopupMenu(self)
        self.fileMenu.insertSeparator()
        self.exitAction.addTo(self.fileMenu)
        self.MenuBar.insertItem("",self.fileMenu,0)

        self.editMenu = QPopupMenu(self)
        self.editPasteAction.addTo(self.editMenu)
        self.editMenu.insertSeparator()
        self.MenuBar.insertItem("",self.editMenu,1)

        self.helpMenu = QPopupMenu(self)
        self.helpHelpAction.addTo(self.helpMenu)
        self.MenuBar.insertItem("",self.helpMenu,2)



        self.languageChange()

        self.resize(QSize(491,490).expandedTo(self.minimumSizeHint()))

        self.connect(self.editPasteAction,SIGNAL("activated()"),self.editPaste)
        self.connect(self.descriptionListBox,SIGNAL("highlighted(QListBoxItem*)"),self.descSelectedSlot)
        self.connect(self.exitAction,SIGNAL("activated()"),self,SLOT("close()"))
        self.connect(self.descriptionListBox,SIGNAL("doubleClicked(QListBoxItem*)"),self.editPaste)

    def languageChange(self):
        self.setCaption(self.tr("Kodos - Regex Library"))
        self.groupBox5.setTitle(self.tr("Description"))
        self.tabWidget3.changeTab(self.tab,self.tr("Regex"))
        self.textLabel3.setText(self.tr("Contributed By:"))
        self.tabWidget3.changeTab(self.tab_2,self.tr("Notes"))
        self.editPasteAction.setText(self.tr("Paste"))
        self.editPasteAction.setMenuText(self.tr("&Paste Example Into Kodos"))
        self.editPasteAction.setToolTip(self.tr("Paste This Example Into Kodos"))
        self.editPasteAction.setAccel(self.tr("Ctrl+V"))
        self.helpHelpAction.setText(self.tr("Help"))
        self.helpHelpAction.setMenuText(self.tr("&Help"))
        self.helpHelpAction.setAccel(self.tr("Ctrl+/"))
        self.exitAction.setText(self.tr("Exit"))
        self.exitAction.setMenuText(self.tr("&Exit"))
        self.toolBar.setLabel(self.tr("Tools"))
        self.MenuBar.findItem(0).setText(self.tr("&File"))
        self.MenuBar.findItem(1).setText(self.tr("&Edit"))
        self.MenuBar.findItem(2).setText(self.tr("&Help"))

    def fileNew(self):
        print "RegexLibraryBA.fileNew(): Not implemented yet"

    def fileOpen(self):
        print "RegexLibraryBA.fileOpen(): Not implemented yet"

    def fileSave(self):
        print "RegexLibraryBA.fileSave(): Not implemented yet"

    def fileSaveAs(self):
        print "RegexLibraryBA.fileSaveAs(): Not implemented yet"

    def filePrint(self):
        print "RegexLibraryBA.filePrint(): Not implemented yet"

    def fileExit(self):
        print "RegexLibraryBA.fileExit(): Not implemented yet"

    def editUndo(self):
        print "RegexLibraryBA.editUndo(): Not implemented yet"

    def editRedo(self):
        print "RegexLibraryBA.editRedo(): Not implemented yet"

    def editCut(self):
        print "RegexLibraryBA.editCut(): Not implemented yet"

    def editCopy(self):
        print "RegexLibraryBA.editCopy(): Not implemented yet"

    def editPaste(self):
        print "RegexLibraryBA.editPaste(): Not implemented yet"

    def editFind(self):
        print "RegexLibraryBA.editFind(): Not implemented yet"

    def helpIndex(self):
        print "RegexLibraryBA.helpIndex(): Not implemented yet"

    def helpContents(self):
        print "RegexLibraryBA.helpContents(): Not implemented yet"

    def helpAbout(self):
        print "RegexLibraryBA.helpAbout(): Not implemented yet"

    def descSelectedSlot(self):
        print "RegexLibraryBA.descSelectedSlot(): Not implemented yet"
