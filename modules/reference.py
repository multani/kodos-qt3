#  reference.py: -*- Python -*-  DESCRIPTIVE TEXT.

from qt import *
from referenceBA import *
from util import *
import xpm
from tooltip import *
#from status_bar import *


class Reference(ReferenceBA):
    def __init__(self, parent, kodos):
        ReferenceBA.__init__(self, parent)
        self.kodos = kodos

    def copy_symbol_slot(self):
        list_view_item = self.referenceListView.selectedItem()
        if list_view_item == None:
            return
        
        symbol = str(list_view_item.text(0))
        self.kodos.emit(PYSIGNAL('copySymbol()'), (symbol,))

        

class ReferenceWindow(QMainWindow):
    def __init__(self, parent, flags=None):
        QMainWindow.__init__(self, None, None,
                             Qt.WDestructiveClose | Qt.WType_TopLevel)

        self.kodos = parent
        self.ref = Reference(self, self.kodos)

        
        self.setGeometry(200, 20, 550, 720)
        self.setCaption("Kodos: Python Regex Reference")

        self.setIcon(getPixmap("kodos_icon.png", "PNG"))

        self.createMenuBar()
        self.createToolBar()

        self.setCentralWidget(self.ref)
        self.show()



    def createToolBar(self):
        toolbar = QToolBar(self)
        toolbar.setStretchableWidget(self.menubar)

        self.closePixmap = QPixmap(xpm.closeIcon)
        self.closeButton = QToolButton(toolbar, "closebutton")
        self.closeButton.setPixmap(self.closePixmap)
        self.closeTooltip = Tooltip("Close regex reference window")
        self.closeTooltip.addWidget(self.closeButton)
        self.connect(self.closeButton, SIGNAL("clicked()"), self.close)

        toolbar.addSeparator()

        self.copyButton = QToolButton(toolbar, "copy")
        self.copyButton.setPixmap(QPixmap(xpm.copyIcon))
        self.copyTip = Tooltip("Copy selected symbol to regex entry")
        self.copyTip.addWidget(self.copyButton)
        self.connect(self.copyButton, SIGNAL("clicked()"), self.ref.copy_symbol_slot)
    
        self.logolabel = kodos_toolbar_logo(toolbar)
                

    def createMenuBar(self):
         # create a menubar
        self.menubar = QMenuBar(self)
        self.menubar.setSeparator(1)

        # populate "File" 
        self.filemenu = QPopupMenu()

        self.filemenu.insertItem(QIconSet(QPixmap(xpm.closeIcon)),
                                 "&Close Regex Reference Window", self.close)
        
        self.menubar.insertItem("&File", self.filemenu)


        self.editmenu = QPopupMenu()
        self.copyid = self.editmenu.insertItem(QIconSet(QPixmap(xpm.copyIcon)),
                                               "&Copy symbol to regex entry",
                                               self.ref.copy_symbol_slot, Qt.CTRL+Qt.Key_C )

        self.menubar.insertItem("&Edit", self.editmenu)

        # populate "Help"
        self.helpmenu = QPopupMenu()
        self.id = self.helpmenu.insertItem(QIconSet(QPixmap(xpm.helpIcon)),
                                           "&Help", self.kodos.helpHelp)
        self.id = self.helpmenu.insertItem(QIconSet(QPixmap(xpm.pythonIcon)),
                                           "&Python regex help", self.kodos.helpPythonRegex)
        self.helpmenu.insertSeparator()
        self.id = self.helpmenu.insertItem("&About...", self.kodos.helpAbout)
        self.menubar.insertItem("&Help", self.helpmenu)       


