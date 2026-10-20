text = input("введите числа через пробел: ")

numbers = []
for item in text.split():
    if "." in item:
        numbers.append(float(item))
    else:
        numbers.append(int(item))

print(f"введенные числа: {numbers}")

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(f"уникальные числа: {unique}")

repeated = []
for number in unique:
    count = 0
    for other in numbers:
        if other == number:
            count += 1
    if count > 1:
        repeated.append(number)
print(f"повторяющиеся числа: {repeated}")

even = []
odd = []
for number in numbers:
    if isinstance(number, int):
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
print(f"четные числа: {even}")
print(f"нечетные числа: {odd}")

negative = []
for number in numbers:
    if number < 0:
        negative.append(number)
print(f"отрицательные числа: {negative}")

floats = []
for number in numbers:
    if isinstance(number, float):
        floats.append(number)
print(f"числа с плавающей точкой: {floats}")

sum_five = 0
for number in numbers:
    if number % 5 == 0:
        sum_five += number
print(f"сумма чисел, кратных 5: {sum_five}")

biggest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number
print(f"самое большое число: {biggest}")
print(f"самое маленькое число: {smallest}")
