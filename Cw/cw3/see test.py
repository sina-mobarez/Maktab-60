n = int(input('num:'))
a = input('vocab :')
b = input('yr guess: ')
wrong = 0
if len(a) == n and len(b) == n :
    for i in range(n):
        if a[i] != b[i]:
            wrong += 1
    # i = 0
    # wrong = 0
    # while i < n :
    #     if a[i] == b[i]:
    #         pass
    #     else:
    #         wrong += 1
    #     i += 1
    print(wrong)

else:
    print('not equal')

