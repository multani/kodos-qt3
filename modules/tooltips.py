#  tooltips.py: -*- Python -*-  DESCRIPTIVE TEXT.

from qt import *
from tooltip import *

def create_kodos_tooltips(kodosWidget):

        kodosWidget.ignoreTooltip = Tooltip("""Perform case-insensitive matching; expressions like [A-Z] will match
lowercase letters, too. This is not affected by the current locale.""")
        kodosWidget.ignoreTooltip.addWidget(kodosWidget.ignorecaseCheckBox)

        kodosWidget.multilineTooltip = Tooltip("""When specified, the pattern character "^" matches at the beginning of the 
string and at the beginning of each line (immediately following each newline); 
and the pattern character "$" matches at the end of the string and at the end 
of each line (immediately preceding each newline). By default, "^" matches 
only at the beginning of the string, and "$" only at the end of the string and 
immediately before the newline (if any) at the end of the string.""")
        kodosWidget.multilineTooltip.addWidget(kodosWidget.multilineCheckBox)

        kodosWidget.dotallTooltip = Tooltip("""Make the "." special character match any character at all, including a 
newline; without this flag, "." will match anything except a newline.""")
        kodosWidget.dotallTooltip.addWidget(kodosWidget.dotallCheckBox)

        kodosWidget.unicodeTooltip = Tooltip("""Make \w, \W, \b, and \B dependent on the Unicode character properties 
database. New in version 2.0. """)
        kodosWidget.unicodeTooltip.addWidget(kodosWidget.unicodeCheckBox)

        kodosWidget.verboseTooltip = Tooltip("""This flag allows you to write regular expressions that look nicer. Whitespace 
within the pattern is ignored, except when in a character class or preceded by 
an unescaped backslash, and, when a line contains a "#" neither in a character
class or preceded by an unescaped backslash, all characters from the leftmost 
such "#" through the end of the line are ignored.""")
        kodosWidget.verboseTooltip.addWidget(kodosWidget.verboseCheckBox)

        kodosWidget.localeTooltip = Tooltip("""Make \w, \W, \b, and \B dependent on the current locale. """)
        kodosWidget.localeTooltip.addWidget(kodosWidget.localeCheckBox)
