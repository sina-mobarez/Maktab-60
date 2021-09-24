n = int(input('yr nu of point:'))
toge = [tuple(map(int, input().split(' '))) for i in range(n)]
print(toge)
lst = []
for i in range(n-1):
   for j in range(n-1):
        y = abs(toge[i][0]-toge[i+1][0]) + abs(toge[i][1]-toge[i+1][1])
        lst.append(y)
print(lst)
print(max(lst))