import os

# get directory from user
path = input('enter your directory :')

# recognize files in directory and appending text of files in a new file
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            with open(entry, 'r') as reader:
                file = reader.read()
                with open('all_text.txt', 'a+') as appending:
                    appending.write(file)

# sorted by alphabet and show 5 second lines
with open('all_text.txt', 'r+') as reader:
    print(sorted(reader)[4:9])

