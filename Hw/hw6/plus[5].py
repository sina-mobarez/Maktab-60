list_1 = [100, 200, 300, 400, 500]
list_2 = [1, 10, 100, 1000, 10000]

# using lambda function to plus 2 element of 2 lists
plus = list(map(lambda x, y: x + y, list_1, list_2))
print(plus)
