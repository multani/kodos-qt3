#!/usr/bin/env python
from modules.version import VERSION
try:
    import py2exe
    HAS_PY2EXE = 1
except:
    HAS_PY2EXE = 0
    
from distutils.core import setup
import os
import os.path
import sys
from glob import glob

args = sys.argv[1:]

kodos_path = os.path.join(sys.prefix, "kodos")

for arg in args:
    if arg == "--formats=wininst":
        kodos_path = "kodos"

HELP_DIR = os.path.join(kodos_path, "help")
HELP_PY_DIR = os.path.join(kodos_path,  "help", "python")
IMAGES_DIR = os.path.join(kodos_path, "images")
SCREENSHOTS_DIR = os.path.join(kodos_path, "screenshots")
MODULES_DIR = os.path.join(kodos_path, "modules")

#########################################################################

setup(name="kodos",
      version=VERSION,
      description="Kodos is a visual regular expression editor",
      author="Phil Schwartz",
      author_email="phil_schwartz@users.sourceforge.net",
      url="http://kodos.sourceforge.net",
      scripts=['kodos.py'],
      packages=['modules', '.'],
      data_files=[(HELP_DIR, glob("help/*.html")),
                  (HELP_PY_DIR, glob("help/python/*.html")),
                  (IMAGES_DIR, glob("images/*.png")),
                  (SCREENSHOTS_DIR, glob("screenshots/*.png")),
                  (kodos_path, ['kodos.bap']),
                  (MODULES_DIR, glob("modules/*.ui")),
##                  (MODULES_DIR, glob("modules/*.py")),
##                  (kodos_path, ['kodos.py']),
                  ],
      license="GPL",
      extra_path='kodos',
      long_description="""
      Kodos is a visual regular expression editor and debugger.
      """
      )

