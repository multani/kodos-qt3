# Form implementation generated from reading ui file '/www/kodos/modules/referenceBA.ui'
#
# Created: Tue Feb 18 10:06:44 2003
#      by: The Python User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *


class ReferenceBA(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if name == None:
            self.setName('ReferenceBA')

        self.resize(585,535)
        self.setCaption(self.tr('Reference Guide'))
        ReferenceBALayout = QGridLayout(self)
        ReferenceBALayout.setSpacing(6)
        ReferenceBALayout.setMargin(11)

        self.referenceListView = QListView(self,'referenceListView')
        self.referenceListView.addColumn(self.tr('Symbol'))
        self.referenceListView.addColumn(self.tr('Definition'))
        item = QListViewItem(self.referenceListView,None)
        item.setText(0,self.tr('.'))
        item.setText(1,self.tr('Matches any character'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('*'))
        item.setText(1,self.tr('Matches 0 or more repetition of preceeding RE'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('+'))
        item.setText(1,self.tr('Matches 1 or more repetition of preceeding RE'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('?'))
        item.setText(1,self.tr('Matches 0 or 1 repetition of preceeding RE'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('^'))
        item.setText(1,self.tr('Matches start of string'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('$'))
        item.setText(1,self.tr('Matches the end of the string'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\A'))
        item.setText(1,self.tr('Matches only at the start of the string'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\B'))
        item.setText(1,self.tr('Matches the empty string, but only when it is not at the beginning or end of a  word'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\b'))
        item.setText(1,self.tr('Matches the empty string, but only at the beginning or end of a word'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\d'))
        item.setText(1,self.tr('Matches any decimal digit'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\D'))
        item.setText(1,self.tr('Matches any non-digit character'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\z'))
        item.setText(1,self.tr('Matches only at the end of the string'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\W'))
        item.setText(1,self.tr('Matches any non-word'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\w'))
        item.setText(1,self.tr('Matches any word'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\S'))
        item.setText(1,self.tr('Matches any non-whitespace character'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\s'))
        item.setText(1,self.tr('Matches any whitespace character'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('\\\\'))
        item.setText(1,self.tr('Matches a literal backslash'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('??'))
        item.setText(1,self.tr('Non-greedy ?'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('*?'))
        item.setText(1,self.tr('Non-greedy *'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('+?'))
        item.setText(1,self.tr('Non-greedy +'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('()'))
        item.setText(1,self.tr('Capturing Parenthesis'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('(?:)'))
        item.setText(1,self.tr('Non-capturing Parenthesis'))

        item = QListViewItem(self.referenceListView,item)
        item.setText(0,self.tr('[]'))
        item.setText(1,self.tr('Character class'))

        self.referenceListView.setSizePolicy(QSizePolicy(5,5,self.referenceListView.sizePolicy().hasHeightForWidth()))
        self.referenceListView.setFrameShape(QListView.StyledPanel)
        self.referenceListView.setFrameShadow(QListView.Sunken)
        self.referenceListView.setVScrollBarMode(QListView.Auto)
        self.referenceListView.setHScrollBarMode(QListView.Auto)
        self.referenceListView.setAllColumnsShowFocus(1)

        ReferenceBALayout.addWidget(self.referenceListView,0,0)

        self.connect(self.referenceListView,SIGNAL('doubleClicked(QListViewItem*)'),self.copy_symbol_slot)

    def copy_symbol_slot(self):
        print 'ReferenceBA.copy_symbol_slot(): not implemented yet'
