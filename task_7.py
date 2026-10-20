BASE_PRICE = 24.99
FREE_MINUTES = 60
FREE_SMS = 30
FREE_MB = 1024  # 1 ГБ = 1024 МБ
PRICE_MINUTE = 0.89
PRICE_SMS = 0.59
PRICE_MB = 0.79
TAX = 0.02

minutes = int(input("сколько минут разговора использовано: "))
sms = int(input("сколько смс отправлено: "))
mb = int(input("сколько интернет-трафика использовано (в МБ): "))

print()
print(f"базовая стоимость тарифа: {BASE_PRICE:.2f} руб.")
total = BASE_PRICE

if minutes > FREE_MINUTES:
    extra_minutes = minutes - FREE_MINUTES
    extra_minutes_sum = extra_minutes * PRICE_MINUTE
    total += extra_minutes_sum
    print(f"дополнительные минуты ({extra_minutes} шт.): {extra_minutes_sum:.2f} руб.")

if sms > FREE_SMS:
    extra_sms = sms - FREE_SMS
    extra_sms_sum = extra_sms * PRICE_SMS
    total += extra_sms_sum
    print(f"дополнительные сообщения ({extra_sms} шт.): {extra_sms_sum:.2f} руб.")

if mb > FREE_MB:
    extra_mb = mb - FREE_MB
    extra_mb_sum = extra_mb * PRICE_MB
    total += extra_mb_sum
    print(f"дополнительный интернет-трафик ({extra_mb} МБ): {extra_mb_sum:.2f} руб.")

tax_sum = total * TAX
final_sum = total + tax_sum

print(f"сумма без налога: {total:.2f} руб.")
print(f"налог (2%): {tax_sum:.2f} руб.")
print(f"итого к оплате: {final_sum:.2f} руб.")
