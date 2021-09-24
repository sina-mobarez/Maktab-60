lst = [[34587, 'Learning Python', 'Mark Lutz', 4, 40.95],
       [98762, 'Programming Python', 'Mark Lutz', 5, 56.80],
       [77226, 'Head First Python', 'Paul Barry', 3, 32.95],
       [88112, 'Einführung in Python3', 'Bernd Klein', 3, 24.99]
       ]
print("Order Summary: ", list(
    map(lambda x: (x[0], x[-1]) if x[-1] * x[-2] > 100 else x[-1] * x[-2] + 10, lst)))
