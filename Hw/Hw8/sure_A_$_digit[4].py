import re

text = input('enter your text : ')


def find(text):
    if re.search('[0-9]', text) and re.search('A', text) and re.search('\$', text):
        return True
    else:
        return False


if find(text):
    print('your text have A , $ and digit ')
else:
    print('sorry seems doesnt exist all of that')
