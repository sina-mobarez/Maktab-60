x = 1
n = int(input('number:'))
for i in range(1, n+1):
    print('')
    for j in range(1, n+1):
      x = i * j
      print((x), end='\t')
