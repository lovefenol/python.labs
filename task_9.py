types = {
    "длина": {
        "мм": 0.001,
        "см": 0.01,
        "м": 1,
        "км": 1000,
        "дюйм": 0.0254,
        "фут": 0.3048,
        "миля": 1609.344,
    },
    "масса": {
        "г": 1,
        "кг": 1000,
        "т": 1000000,
        "фунт": 453.592,
    },
    "время": {
        "сек": 1,
        "мин": 60,
        "час": 3600,
        "сутки": 86400,
    },
    "объем": {
        "мл": 0.001,
        "л": 1,
        "м3": 1000,
    },
}

temperature_units = ["C", "K", "F"]

print("доступные типы измерения: длина, масса, время, объем, температура")
for type_name in types:
    print(f"  {type_name}: {', '.join(types[type_name])}")
print(f"  температура: {', '.join(temperature_units)}")
print()

type_name = input("введите тип измерения: ")
from_unit = input("введите исходную единицу: ")
to_unit = input("введите целевую единицу: ")
value = float(input("введите значение: "))

if type_name == "температура":
    if from_unit == "C":
        celsius = value
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        celsius = (value - 32) * 5 / 9

    if to_unit == "C":
        result = celsius
    elif to_unit == "K":
        result = celsius + 273.15
    else:
        result = celsius * 9 / 5 + 32
else:
    base_value = value * types[type_name][from_unit]
    result = base_value / types[type_name][to_unit]

print(f"результат: {value} {from_unit} = {result:.4f} {to_unit}")
