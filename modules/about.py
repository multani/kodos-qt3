#  about.py: -*- Python -*-  DESCRIPTIVE TEXT.

from qt import *
from aboutBA import *
from util import getPixmap
import version

class About(AboutBA):
    def __init__(self):
        AboutBA.__init__(self)
        self.versionLabel.setText(version.VERSION)


