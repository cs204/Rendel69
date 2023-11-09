menu = {
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50
}

def calculate_total_cost(order):
    total_cost = 0.0
    for item in order:
        if item in menu:
            total_cost += menu[item]
    return total_cost

order = []

try:
    while True:
        dish = input("Блюдо: ").strip().lower()
        if dish in menu:
            order.append(dish)
        else:
            print(f"{dish} отсутствует в меню и будет проигнорирован.")
except EOFError:
    pass

total_cost = calculate_total_cost(order)
print(f"Сумма: {total_cost:.2f}")
