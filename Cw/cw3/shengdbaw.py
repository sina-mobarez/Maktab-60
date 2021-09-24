n = int(input('how many time wanna to operate:'))
lst = []
for i in range(n):
    add, value = input('enter yr operate:').split()
    value = int(value)
    if add == 'add':
        lst.append(value)
    elif add == 'ask':
        lst = sorted(lst)
        print(lst[value-1])