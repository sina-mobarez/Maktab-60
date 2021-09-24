# open file and read n lines
n = int(input('lines :'))
with open('txt.txt') as reader:
    for i in range(n):
        print(reader.readline())

# read and append some words in file
with open('txt.txt', 'r') as reader:
    with open('txt.txt', 'a') as appending:
        new_text = 'new text for appending to end of file :)))))) '
        appending.write(new_text)
    print(reader.read())

# open file and read line by line and store it into a list
lst = []
with open('txt.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        lst.append(line)
        line = reader.readline()
print(lst)

# open file and find longest words
with open('txt.txt', 'r') as reader:
    words = reader.read().split()
longest = len(max(words, key=len))
longest_word = [word for word in words if len(word) == longest]
print(longest_word)
