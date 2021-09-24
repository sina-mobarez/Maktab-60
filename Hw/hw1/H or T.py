from random import choice

sekkeh = ['H', 'T']

average = []
counter = 0
string = ''
while True:
    string += choice(sekkeh)
    if len(string) > 2:
        if string[-3:] == 'TTT' or string[-3:] == 'HHH':
            print(f'{string}({len(string)} flips)')
            average.append(len(string))
            counter += 1
            string = ''
    if counter == 10:
        print(f'On average, {sum(average)/10} flips were needed.')
        break