m, n = list(map(int, input('plz enter yr row and pillow:').split()))
lst = []
lst1 = []
lst2 = []
for i in range(m):
    lst.append(list(map(int, input().split())))
print(lst)
for i in range(m):
    lst1.append(list(map(int, input().split())))
print(lst1)
for i in range(m):
    lst2.append([])
    for j in range(n):
        lst2[-1].append(lst[i][j] + lst1[i][j])
print(lst2)