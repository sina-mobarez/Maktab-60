import os
print(os.getcwd())
# get directory from user
path = input('enter your directory ----> ')

# make empty list for file and folders
folders = []
files = []

# append folders in a list
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_dir():
            folders.append(entry.name)

# append files in a list
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            files.append(entry.name)

# show count of files and folders

print(f'Number of files : {len(files)}')
print(f'Number of folders : {len(folders)}')
