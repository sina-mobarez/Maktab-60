import os

path = input('enter your directory :')
try:
    if os.path.isdir(path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        os.chdir(path)
        if len(files) == 0:
            print('This Directory has no any files')
        else:
            print(f'list of your files: {files}')
    else:
        print('This address not found >>>> try again')
        raise TypeError
except TypeError:
    print(" your directory doesn't exist ")


class SkipThisFile(Exception):
    pass


def read_lines(*file):
    for file in files:
        try:
            with open(file) as f:
                for line in f:
                    yield line
        except SkipThisFile:
            yield 0


def display_files(*file):
    source = read_lines(*file)
    for line in source:
        print(line, end='')
        inp = input()
        if inp == 'n':
            print("next")
            source.throw(SkipThisFile)


display_files(files)
