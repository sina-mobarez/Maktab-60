n = int(input('how many want to change:'))

lst = []
for i in range(n):
    add_or_omit, index, *val = input().split()
    ind = int(index)

    if add_or_omit == '+':
        value = list(map(int, val))
        value = value[0]
        lst.insert(ind, value)
        print(lst)
    elif add_or_omit == '-':
        lst.pop(ind)
        print(lst)
    else:
        print('yr input is wrong!')
