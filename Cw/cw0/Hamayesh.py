sitNum = input("yr number of chair: ")
n = int(sitNum)
rowOfSit = input(" yr Row of sit : ")
r = int(rowOfSit)
# print(list(range(1, n)))
# print("--------------------------------")
# print(list(range(10, 0, -1)))
if n >= 1 and n <= 10 :
    print(" go right")
else :
    print(" go left") 

if n >= 1 and n <= 10 :
    print(n)
else :
    nee = 20 - n
    nee += 1
    print(f"your step to go on yr sit : {nee}")   
if r >= 1 and r <= 10 :
    ree = 10 - r
    print(f"your row u must sitt : {ree}")         