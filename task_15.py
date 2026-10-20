sales = [
    {"name": "ноутбук", "price": 50000, "quantity": 3},
    {"name": "мышь", "price": 800, "quantity": 25},
    {"name": "клавиатура", "price": 2500, "quantity": 10},
    {"name": "ноутбук", "price": 50000, "quantity": 2},
    {"name": "монитор", "price": 15000, "quantity": 6},
    {"name": "мышь", "price": 800, "quantity": 5},
]

revenue = {}
for sale in sales:
    name = sale["name"]
    money = sale["price"] * sale["quantity"]
    if name in revenue:
        revenue[name] += money
    else:
        revenue[name] = money

print("выручка по каждому товару:")
for name in revenue:
    print(f"  {name}: {revenue[name]} руб.")

best_name = None
best_money = 0
for name in revenue:
    if best_name is None or revenue[name] > best_money:
        best_name = name
        best_money = revenue[name]
print(f"самый прибыльный товар: {best_name} ({best_money} руб.)")

print(f"количество уникальных наименований: {len(revenue)}")
