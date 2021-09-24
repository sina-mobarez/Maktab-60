import os
# reader = open('loptops.txt')
# print(reader.readlines())
# reader.close()

# with open('loptops.txt') as reader:
    # print(reader.tell())
    # print(reader.read())
    # print(reader.tell())
    # reader.seek(0)
    # print(reader.tell())
    # print(reader.readline())
    # print(reader.tell())
    # reader.seek(0)
    # print(reader.tell())
    # print(reader.readline())
    # print(reader.tell())
    # lines = reader.readlines()
    # print(reader.tell())

    # for line in lines:
    #     print(line)

    # line = reader.readline()
    # while line != '':
    #     print(line)
    #     print(reader.tell())
    #     line = reader.readline()


# with open('new_file.txt', 'r+') as writer:
#     print(writer.readlines())
#     writer.write('This is test text!')

# with open('loptops.txt', 'r') as reader:
#     with open('asus_loptops.txt', 'w') as writer:
#         line = reader.readline()
#         while line != '':
#             if 'Asus' in line:
#                 writer.write(line)
#             line = reader.readline()

# os.rename('loptop.txt', 'loptops.txt')
# os.remove('asus_loptops.txt')
# os.mkdir('test_dir')
# os.rmdir('test_dir')
# print(os.getcwd())
for i in range(6):
    print(' ' * (7 - i) + ' *' * (7 + 1))