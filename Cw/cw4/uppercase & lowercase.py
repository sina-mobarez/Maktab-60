txt = input('enter yr txt :')
lst = []
lst2 = []
for i in txt:
    n = ord(i)
    if n > 64 and n < 91:
        lst.append(n)
    elif n > 96 and n <123:
        lst2.append(n)
dic = {"upperCase": len(lst),
       "lowercase": len(lst2)}
print(dic)