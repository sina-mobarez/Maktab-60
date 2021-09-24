def gcd(x,y):
    if (x < y) :
        temp = x
        x = y
        y = temp
    while (y != 0):
        reminder = x % y
        x = y
        y = reminder
    r = x
    return r

def lcm(a, b) :
    return int(a * b / gcd(a, b))

n = int(input('your number:'))
e = 1
i = 1
for i in range(1, n):
    if gcd(i, n) == 1 :
        e = lcm(e, i)
print(e)
