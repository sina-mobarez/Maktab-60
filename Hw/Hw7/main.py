import bank_account

a = bank_account.Account('sina', 22)
b = bank_account.Account('jamal', 120500)

a.receipt(1200)
a.transfer(b, 4200)
print(b.show_balance)

b.transfer(a, 1230000)
b.transfer(a, 110000)
print(a.show_balance)

