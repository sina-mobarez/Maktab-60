lst1 = list(map(int, input('type yr big list:').split()))
lst2 = list(map(int, input('type array yr sub list:').split()))
def is_ord_sub(lst2,lst1):
    x = ''
    m = 0
    for i in range(len(lst2)):
        if lst2[i] in lst1:
            x = lst2[i]
            y = lst1.index(x)
            if y >= m:
                x = ''
                m = y
                continue
            return False
        else:
            print('Yr sublist is wrong ')
    return True

print(f"is ord sub ({lst2},{lst1}) ={is_ord_sub(lst2,lst1)} ")





# print(f"is ord sub ({lst2},{lst1}) = {cmpre(lst1,lst2)} ")

