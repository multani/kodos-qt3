#!/usr/bin/env python
from modules.version import VERSION
from distutils.core import setup
#from distutils.sysconfig import get_python_lib
import os
import os.path
import sys
from glob import glob

args = sys.argv[1:]

libpath = "/usr/local/kodos"

for arg in args:
    if arg == "--formats=wininst":
        libpath = "kodos"

HELP_DIR = os.path.join(libpath, "help")
HELP_PY_DIR = os.path.join(libpath,  "help", "python")
IMAGES_DIR = os.path.join(libpath, "images")
SCREENSHOTS_DIR = os.path.join(libpath, "screenshots")
MODULES_DIR = os.path.join(libpath, "modules")


#########################################################################

setup(name="kodos",
      version=VERSION,
      description="Kodos is a visual regular expression editor",
      author="Phil Schwartz",
      author_email="phil_schwartz@users.sourceforge.net",
      url="http://kodos.sourceforge.net",
      ##package_dir={'': 'modules'},
      packages=['modules', "."],
      data_files=[(HELP_DIR, glob("help/*.html")),
                  (HELP_PY_DIR, glob("help/python/*.html")),
                  (IMAGES_DIR, glob("images/*.png")),
                  (SCREENSHOTS_DIR, glob("screenshots/*.png")),
                  (libpath, ['kodos.bap']),
                  (MODULES_DIR, glob("modules/*.ui"))
                  ],
      license="GPL",
      extra_path='kodos',
      long_description="""
      Kodos is a visual regular expression editor and debugger.
      """
      )

    
