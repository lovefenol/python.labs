age = int(input("возраст заемщика: "))
income = float(input("ежемесячный доход (руб.): "))
credit = float(input("размер запрашиваемого кредита (руб.): "))
term = int(input("срок кредита (месяцы): "))
history = input("кредитная история (отличная/хорошая/удовлетворительная/плохая): ")
has_guarantor = input("есть поручители? (да/нет): ") == "да"
has_pledge = input("есть залог? (да/нет): ") == "да"

credit_to_income = credit / income
monthly_payment = credit / term
payment_share = monthly_payment / income

print()
print(f"соотношение кредита к доходу: {credit_to_income:.2f}")
print(f"ежемесячный платеж (без процентов): {monthly_payment:.2f} руб.")
print(f"доля платежа от дохода: {payment_share * 100:.1f}%")

points = 0

if age < 21 or age > 65:
    points += 2
elif age < 25:
    points += 1

if credit_to_income > 24:
    points += 3
elif credit_to_income > 12:
    points += 2
elif credit_to_income > 6:
    points += 1

if payment_share > 0.5:
    points += 4
elif payment_share > 0.35:
    points += 3
elif payment_share > 0.2:
    points += 1

if history == "отличная":
    points += 0
elif history == "хорошая":
    points += 1
elif history == "удовлетворительная":
    points += 2
else:
    points += 4

if has_guarantor:
    points -= 1
if has_pledge:
    points -= 2

print(f"баллы риска: {points}")

if points <= 1:
    risk = "низкий"
    rate = 12
elif points <= 4:
    risk = "средний"
    rate = 16
elif points <= 7:
    risk = "высокий"
    rate = 22
else:
    risk = "критический"
    rate = 30

print(f"категория риска: {risk}")
print(f"предлагаемая процентная ставка: {rate}% годовых")

if risk == "низкий" or risk == "средний":
    print("рекомендация: кредит одобрить")
elif risk == "высокий":
    if has_guarantor or has_pledge:
        print("рекомендация: одобрить с осторожностью (есть поручитель или залог)")
    else:
        print("рекомендация: отклонить (высокий риск и нет обеспечения)")
else:
    print("рекомендация: кредит отклонить")
