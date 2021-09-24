a = int(input('number1:'))
b = int(input('number2:'))
a1 = a % 10
a2 = a % 100
a3 = a % 1000
b1 = b % 10
b2 = b % 100
b3 = b % 1000

if a1 > b1 :
    print(str(b)+' < '+str(a))
elif a1 < b1 :
    print(str(a) + ' < ' + str(b))
elif a2 > b2 :
    print(str(b) + ' < ' + str(a))
elif a2 < b2 :
    print(str(a) + ' < ' + str(b))
elif a3 > b3 :
    print(str(b) + ' < ' + str(a))
elif a3 < b3 :
    print(str(a) + ' < ' + str(b))
else :
    print(str(a) + ' = ' + str(b))