#  help.py: -*- Python -*-  DESCRIPTIVE TEXT.

from qt import *
from util import *
import xpm
from webbrowser import launch_browser


class textbrowser(QTextBrowser):
    # reimplemented textbrowser that filters out external sources
    # future: launch web browser
    def __init__(self, parent=None, name=None):
        self.parent = parent
        QTextBrowser.__init__(self, parent, name)


    def setSource(self, src):
        #print "setSource:", src
        s = str(src)
        if s[:7] == 'http://':
            launch_browser(self.parent.external_browser, s)
            return

        QTextBrowser.setSource(self, src)
                
    
                

class Help(QMainWindow):
    def __init__(self, parent, filename, external_browser=None):
        QMainWindow.__init__(self, None, None,
                             Qt.WType_TopLevel | Qt.WDestructiveClose)
        
        self.external_browser = external_browser
        self.setGeometry(100, 50, 800, 600)
        self.setCaption("Help")
        self.setIcon(getPixmap("ssilogo.png", "PNG"))

        self.textBrowser = textbrowser(self)
        absPath = self.getHelpFile(filename)

        self.setCentralWidget(self.textBrowser)
        self.textBrowser.setSource(absPath)
        
        self.createMenu()
        self.createToolBar()
        self.fwdAvailable = 0
        self.show()

        

    def createMenu(self):
        self.filemenu = QPopupMenu()
        self.back = self.filemenu.insertItem("&Back",
                                             self.textBrowser.backward)
        
        self.forward = self.filemenu.insertItem("&Forward",
                                                self.textBrowser.forward)
        
        self.home = self.filemenu.insertItem("&Home", self.textBrowser.home)
        self.filemenu.insertSeparator()
        id = self.filemenu.insertItem("&Close", self, SLOT("close()"))

        self.menubar = QMenuBar(self)
        self.menubar.insertItem("&File", self.filemenu)


    def createToolBar(self):
        toolbar = QToolBar(self)
        toolbar.setStretchableWidget(self.menubar)

        icon_back = QPixmap(xpm.backIcon)
        icon_forward = QPixmap(xpm.forwardIcon)
        icon_home = QPixmap(xpm.homeIcon)


        self.backButton = QToolButton(toolbar, "back")
        self.backPixmap = QPixmap(icon_back)
        self.backButton.setPixmap(self.backPixmap)
        backTooltip = QToolTip(self.backButton)
        backTooltip.add(self.backButton, "Back")
        self.connect(self.backButton, SIGNAL("clicked()"),
                     self.textBrowser.backward)
        

        self.fwdButton = QToolButton(toolbar, "forward")
        self.fwdPixmap = QPixmap(icon_forward)
        self.fwdButton.setPixmap(self.fwdPixmap)
        fwdTooltip = QToolTip(self.fwdButton)
        fwdTooltip.add(self.fwdButton, "Forward")
        #self.connect(self.fwdButton, SIGNAL("clicked()"), self.forwardHandler)
        #self.connect(self.textBrowser, SIGNAL("forwardAvailable(bool)"),
        #             self.setForwardAvailable)
        self.connect(self.fwdButton, SIGNAL("clicked()"), self.textBrowser.forward)


        self.homeButton = QToolButton(toolbar, "home")
        self.homePixmap = QPixmap(icon_home)
        self.homeButton.setPixmap(self.homePixmap)
        homeTooltip = QToolTip(self.homeButton)
        homeTooltip.add(self.homeButton, "Home")
        self.connect(self.homeButton, SIGNAL("clicked()"),
                     self.textBrowser.home)


        self.logolabel = kodos_toolbar_logo(toolbar)
        

    def setForwardAvailable(self, bool):
        #print "bool: ", bool
        self.fwdAvailable = bool


    def forwardHandler(self):
        #print "fwdAvail?: ", self.fwdAvailable
        if self.fwdAvailable:
            self.textBrowser.forward()
    
    def getHelpFile(self, filename):
        return getAppPath() + os.sep + "help" + os.sep + filename
        
