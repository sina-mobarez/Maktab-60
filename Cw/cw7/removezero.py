def rem_zero(lst: list):
    while 0 in lst:
        lst.remove(0)
    print(lst)
    return


def rem_zero_out(lst: list):
    lst_new = [i for i in lst if i != 0]
    print(lst)
    print(lst_new)


lst = [0, 1, 2, 3, 4, 0, 0]
lst2 = [0, 1, 2, 3, 4, 0, 0]
rem_zero(lst)
rem_zero_out(lst2)
