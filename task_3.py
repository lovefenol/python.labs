money = int(input("введите сумму в рублях (целое число): "))
print(f"сумма для размена: {money} руб.")

rest = money

bills_100 = rest // 100
rest = rest % 100

bills_50 = rest // 50
rest = rest % 50

bills_10 = rest // 10
rest = rest % 10

bills_5 = rest // 5
rest = rest % 5

coins_2 = rest // 2
rest = rest % 2

coins_1 = rest

print(f"купюр по 100 руб.: {bills_100}")
print(f"купюр по 50 руб.: {bills_50}")
print(f"купюр по 10 руб.: {bills_10}")
print(f"купюр по 5 руб.: {bills_5}")
print(f"монет по 2 руб.: {coins_2}")
print(f"монет по 1 руб.: {coins_1}")
