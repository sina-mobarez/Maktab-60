import os

# get directory from user and check that exist if not make that
path = input('enter your directory :')
if os.path.exists(path):
    print('your directory already exist')
else:
    os.mkdir(path)
    print('your directory made it now')

