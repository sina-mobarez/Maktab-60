# change a negative number to positive
def change_neg(i):
    i = abs(i)
    return i


# checking if element is negative
def check_neg(i):
    if i < 0:
        return True
    else:
        return False


numbers = [-1000, 500, -600, 700, 5000, -9000, -175000]

# use a filter function to check negative element of list and use map function to change it
neg = list(map(change_neg, (filter(check_neg, numbers))))
