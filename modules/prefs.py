#  prefs.py: -*- Python -*-  DESCRIPTIVE TEXT.

from util import *

class Prefs:
    def __init__(self, parent, autoload=0):
        self.parent = parent
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


    def save(self):
        try:
            fp = open(self.prefsPath, "w")
        except:
            print "Could not save preferences:", self.prefsPath
            return

        print self.prefsPath
        f = self.parent.getfont()

        fp.write("Font: %s:%s:%s:%s:%s:%s\n" %
                 (f.family(), f.pointSize(),
                  f.bold(), f.italic(),
                  f.underline(), f.strikeOut()))
        
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

