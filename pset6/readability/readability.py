from cs50 import get_string

text = get_string("Text: ")

nolet = 0
noword = 1
nosent = 0
i = 0 
n = len(text)
if(text):
    for i in text:
        if (i.isalpha()):
            nolet = nolet + 1
        if(i == ' '):
            noword = noword + 1
        if(i == '.' or i == '!' or i == '?'):
            nosent = nosent + 1
index  = (0.0589 * (100* nolet / noword ) - 0.296 * (100* nosent / noword ) - 15.8)
if (index < 16 and index >= 0):
    print(f"Grade {round(index)}")
elif (index >= 16):
    print("Grade 16+")
else:
    print("Before Grade 1")
#
#
#kept getting string index out of range error