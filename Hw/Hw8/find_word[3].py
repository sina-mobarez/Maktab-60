import re

text = input('enter a text : ')
word = input('enter a word for find : ')


def find(word, text):
    if re.search(f"{word}\Z", text):
        return print(f'find')
    else:
        return print(f'your entered word doesnt exist')


find(word, text)
