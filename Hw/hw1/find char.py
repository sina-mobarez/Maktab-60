# read text file
from collections import Counter
file = open("abc.txt", "r").read() ### you can put any txt file here
x = Counter(file)
print(x)