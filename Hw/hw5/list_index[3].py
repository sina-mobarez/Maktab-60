the_list = list(input('enter the list :').split())
index = int(input('enter the index :'))


def print_list_element(the_list, index):
    try:
        print(the_list[index])
    except IndexError:
        print(f'your index {index} , is out of range >>> try again')
    else:
        print('your order is do now :))))))) ')


print_list_element(the_list, index)
