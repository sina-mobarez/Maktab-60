import random

lst = list(map(int, input('enter 5 number:').split()))
lst2 = []
for j in range(5):
    for i in range(5):
        rnd = random.choice(lst)
        rnd = str(rnd)
        lst2.append(rnd)
    x = "".join(lst2)
    x = int(x)
    print(x)
    lst2 = []
