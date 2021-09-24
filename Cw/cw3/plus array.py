n = int(input('len of list:'))
lst = list(map(int, input('first list:').split()))
lst2 = list(map(int, input('second list:').split()))
for i in range(n):
   print(lst[i]+lst2[i], end=" ")