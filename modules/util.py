#  util.py: -*- Python -*-  DESCRIPTIVE TEXT.

import os
import os.path
import sys
import time
import string
from qt import *
from debug import *

# QT constants that should be defined
FALSE = 0
TRUE = 1

global debug


def get_time(timestr):
    "returns a string representation of the epoch or empty string"
    if timestr == "": return ""

    try:
        epoch = time.mktime(time.strptime(timestr, "%m/%d/%Y"))
    except:
        return ""

    return str(long(epoch))


def get_time_str(epoch_str, format="%m/%d/%Y"):
    if epoch_str == "": return ""

    tm = time.localtime(int(epoch_str))
    timestr = time.strftime(format, tm)
    return timestr


def getAppPath():
    "Convenience function so that we can find the necessary images"
    fullpath = os.path.abspath(sys.argv[0])
    path = os.path.dirname(fullpath)
    return path


def getPixmap(fileStr, fileType="PNG", dir="images"):
    """Return a QPixmap instance for the file fileStr relative
    to the binary location and residing in it's 'images' subdirectory"""

    image = getAppPath() + os.sep + dir + os.sep + fileStr

    if debug & DEBUG_PIXMAP: print "image:", image
    
    pixmap = QPixmap(image, fileType)
    pixmap.setMask(pixmap.createHeuristicMask(1))
    
    return pixmap

    

def dictList_to_CSV(filename, keyList, dictList):
    "creates a file of comma-seperated-values using the keysList as the first line"
    try:
        file = open(filename, "w")
    except:
        QMessageBox.warning(None, "Warning",
                            "Could not write file: %s" % filename)
        return 0
    
    # output the line of headers 
    i = 0
    numKeys = len(keyList)
    for i in range(numKeys):
        file.write('"%s"' % keyList[i])
        if i < numKeys - 1:
            file.write(',')
        else:
            file.write('\n')

    # output the rows of data
    for dict in dictList:
        i = 0
        for i in range(numKeys):
            file.write('"%s"' % dict[keyList[i]])
            if i < numKeys - 1:
                file.write(',')
            else:
                file.write('\n')

    file.close()
    return 1


def dictList_to_XML(filename, keyList, dictList):
    """creates a file consisting of XML.  keylist is a list of the columns (keys)
    in dictList.  Each dict in dictList is written as an item-node"""
    try:
        file = open(filename, "w")
    except:
        QMessageBox.warning(None, "Warning",
                            "Could not write file: %s" % filename)
        return 0

    for dict in dictList:
        file.write("<ITEM>\n")
        for key in keyList:
            file.write("\t<%s>%s</%s>\n" % (key, dict[key], key))
        file.write("</ITEM>\n")
                
    file.close()
    return 1


def getHomeDirectory():
    "attempt to get the home directory... not sure how this behaves w/ Windoze"
    if sys.platform != "win32":
        try:
            homedir = os.environ["HOME"]
        except KeyError:
            homedir = "/tmp"
    else:
        homedir = ""
    
    return homedir


def getComboItem(qComboBox, text, not_found = -1, case_sensitive = 1):
    """returns the item number in the qComboBox for the given text string.
    If the text string is not found in the qComboBox, not_found is returned"""

        
    for i in range(qComboBox.count()):
        itemstr = str(qComboBox.text(i))
        #print itemstr, "-", text, "-"
        if not case_sensitive:
            itemstr = string.upper(itemstr)
            text = string.upper(text)
            
        if itemstr == text:
            return i
    return not_found

    
def getListBoxItem(qListBox, text, not_found = -1):
    for i in range(qListBox.count()):
        itemstr = str(qListBox.text(i))
        if itemstr == text:
            return i
    return not_found

def escapeSQL(s):
    s = string.replace(s, "'", "\\'")
    return s

def escapeSQLq(qstr):
    s = str(qstr)
    return escapeSQL(s)


def kodos_toolbar_logo(toolbar):
    # hack to move logo to right
    blanklabel = QLabel("", toolbar)
    toolbar.setStretchableWidget(blanklabel)
    
    logolabel = QLabel("kodos_logo", toolbar)
    
    logolabel.setText("Kodos   ")
    font = QFont(logolabel.font())
    font.setFamily('helvetic')
    font.setBold(1)
    logolabel.setFont(font)
        
    cg = QColorGroup()
    pal =  logolabel.palette()
    cg.setColor(QColorGroup.Foreground,QColor(9,86,16))
    pal.setActive(cg)
    pal.setInactive(cg)
    logolabel.setPalette(pal)
    return logolabel
