
numbers = input().split()
L, R = int(numbers[0]), int(numbers[1])

string = '1'
for item in range(10):
    for str in string:
        if str == '1':
            string += '0'
        else:
            string += '1'

print(string[L-1:R])