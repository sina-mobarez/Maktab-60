import os
import shutil

# get directory from user
path = input('enter your directory that you want to check ascii text file and "a" exist in their name: ')

# directory for copy of choose by script
path_for_copy = input('enter a directory for copy file that you want :')

# checking all of them that have "a" in their name and contain ascii text and copy them to second directory you write
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            name = entry.name
            for i in name:
                if i == "a":
                    with open(entry, 'rb') as reading:
                        if reading.read().isascii():
                            shutil.copy(entry, path_for_copy)
                break

