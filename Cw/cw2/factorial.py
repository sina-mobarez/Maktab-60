x = int(input('number:'))
n = 1
if x < 0 :
    print('factorial is not defined for negetive number')
elif x == 0 :
    print('factorial for 0 is 1 ')
else :
     for i in range(1,x+1) :
        n = i * n
     print(f'factorial for {x} is {n} ')
