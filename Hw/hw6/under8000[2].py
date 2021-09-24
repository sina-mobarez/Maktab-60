# define a function for checking number and plus
def check_and_plus(i):
    if i < 8000:
        i += 2000
        return i
    else:
        return i


# create a list for test
numbers = [1000, 500, 600, 700, 5000, 90000, 175000]

# use map function to operate it
newList = list(map(check_and_plus, numbers))

print(newList)

