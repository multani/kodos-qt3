#  prefs.py: -*- Python -*-  DESCRIPTIVE TEXT.

from util import *
from prefsBA import PrefsBA

##class Prefs(PrefsBA):
##    def __init__(self, parent=None, name=None, modal=0):
##        print type(self)
##        PrefsBA.__init__(self, parent, name, modal)
##        self.parent = parent
        
class Preferences(PrefsBA):
    def __init__(self, parent, autoload=0):
        self.parent = parent
        PrefsBA.__init__(self, parent)

        prefsFilename = ".kodos"
        self.prefsPath = getHomeDirectory() + os.sep + prefsFilename
        if autoload: self.load()
        
    def load(self):
        try:
            fp = open(self.prefsPath, "r")
        except:
            return
        
        prefsList = fp.readlines()
        for pref in prefsList:
            preference, setting = string.split(pref, ":", 1)
            setting = string.strip(setting)
            if preference == 'Font' and setting:
                self.parseFontStr(setting)
            if preference == 'Web Browser' and setting:
                self.browserEdit.setText(setting)
            if preference == 'Email Server' and setting:
                self.emailServerEdit.setText(setting)


    def save(self):
        try:
            fp = open(self.prefsPath, "w")
        except:
            print "Could not save preferences:", self.prefsPath
            return

        #print self.prefsPath
        f = self.parent.getfont()

        fp.write("Font: %s:%s:%s:%s:%s:%s\n" %
                 (f.family(), f.pointSize(),
                  f.bold(), f.italic(),
                  f.underline(), f.strikeOut()))

        fp.write("Web Browser: %s\n" % str(self.browserEdit.text()))
        fp.write("Email Server: %s\n" % str(self.emailServerEdit.text()))
        fp.close()

                                

    def parseFontStr(self, fontstr):
        # parse a font in the form: family:pt size:bold:italic:underline:strikeout
        parts = string.split(fontstr, ":")
        if len(parts) != 6: return
        
        f = QFont()
        f.setFamily(parts[0])
        f.setPointSize(int(parts[1]))
        f.setBold(int(parts[2]))
        f.setItalic(int(parts[3]))
        f.setUnderline(int(parts[4]))
        f.setStrikeOut(int(parts[5]))
        self.parent.setfont(f)


    def setFontButtonText(self, font):
        self.fontButton.setText("%s %s" % (str(font.family()),font.pointSize() ))

    def showPrefsDialog(self):
        f = self.parent.getfont()
        self.fontButton.setFont(f)
        self.setFontButtonText(f)

        self.show()

    def font_slot(self):
        (font, ok) = QFontDialog.getFont(self.fontButton.font())
        if ok:
            self.fontButton.setFont(font)
            self.setFontButtonText(font)


    def browser_slot(self):
        fn = QFileDialog.getOpenFileName(self.browserEdit.text(), "All (*)",
                                         self, "Choose Web Browser")
        if not fn.isEmpty():
            self.browserEdit.setText(fn)


    def apply_slot(self):
        self.parent.setfont(self.fontButton.font())
        self.save()


    def accept(self):
        self.apply_slot()
        QDialog.accept(self)


    def help_slot(self):
        self.helpWindow = help.Help(self, "prefa.html")

