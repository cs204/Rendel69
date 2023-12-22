calories = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Lime": 20
}
fruit = input("Фрукт: ")
if fruit in calories:
    print(f"Калории: {calories[fruit]}")
