# n words get and reverse print
howManyWords = input(" how many words you want to enter? ")
nWords = int(howManyWords)
# data_list = []
# while True :
#     data = input("enter your word : ")
#     if data == "//" :
#         break
#     data_list += [data]

# print(data_list)

sttt = input(" your words : ")
My_List_1 = list(sttt.split(' '))


print(*My_List_1, sep=' ')

print('\n')

My_List_1.reverse()
print(*My_List_1, sep=' ')