import re

num = input('enter a phone number : ')


def validation_phone_number(number):
    if re.search('\A\+989\d{9}', number):
        print(f'09{number[4:]}')

    elif re.search('\A\+00989\d{9}', number):
        print(f'09{number[6:]}')

    elif re.search('\A00989\d{9}', number):
        print(f'09{number[5:]}')

    elif re.search('\A\+0989\d{9}', number):
        print(f'09{number[5:]}')

    elif re.search('\A09\d{9}', number):
        print(f'{number}')
    else:
        print('invalid phone number')


validation_phone_number(num)
