#!python3
#bulletPointAdder.py -Add Wikipedia bullet points to the start
#of each line of the clipboard
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyperclip
text=pyperclip.paste()
#Seperate lines and add stars
lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)
