a = int(input('number1:'))
b = int(input('number2:'))
c = int(input('number3:'))
d = int(input('number4:'))

if a > b and a > c and a > d :
    print(f'{a} is maximum')
elif b > c and b > a and b > d :
    print('maximum is', b)
elif c > a and c > b and c > d :
    print('maximum is:', c)
elif d > a and d > b and d > c :
    print('maximum is:', d)
else :
    print("all your number is equal")

