amount = float(input("сумма покупки (руб.): "))
age = int(input("возраст покупателя: "))
birthday_answer = input("сегодня день рождения покупателя? (да/нет): ")
vip_answer = input("клиент VIP? (да/нет): ")

is_birthday = birthday_answer == "да"
is_vip = vip_answer == "да"

discount = 0
if amount > 1000:
    discount += 10
    print("скидка за сумму покупки больше 1000 руб.: 10%")
if age >= 63:
    discount += 5
    print("скидка пенсионеру: 5%")
if is_birthday:
    discount += 5
    print("скидка в день рождения: 5%")

if is_vip:
    print("VIP-скидка: 15% (не суммируется, берется большая из скидок)")
    if discount < 15:
        discount = 15

if discount > 25:
    discount = 25
    print("скидка ограничена максимумом в 25%")

discount_sum = amount * discount / 100
final_sum = amount - discount_sum

print()
print(f"итоговая скидка: {discount}%")
print(f"сумма скидки: {discount_sum:.2f} руб.")
print(f"сумма к оплате: {final_sum:.2f} руб.")
