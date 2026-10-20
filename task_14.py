def read_numbers(text):
    result = []
    for item in text.split():
        if "." in item:
            result.append(float(item))
        else:
            result.append(int(item))
    return result


first = read_numbers(input("введите первый набор чисел через пробел: "))
second = read_numbers(input("введите второй набор чисел через пробел: "))

print(f"первый набор: {first}")
print(f"второй набор: {second}")

both = []
for number in first:
    if number in second and number not in both:
        both.append(number)
print(f"числа в обоих наборах: {both}")

only_first = []
for number in first:
    if number not in second and number not in only_first:
        only_first.append(number)

only_second = []
for number in second:
    if number not in first and number not in only_second:
        only_second.append(number)

print(f"есть в первом, но нет во втором: {only_first}")
print(f"есть во втором, но нет в первом: {only_second}")

others = []
for number in first + second:
    if number not in both and number not in others:
        others.append(number)
print(f"числа из обоих наборов без общих: {others}")
