import requests
import sys

def get_bitcoin_price(n):
    try:
        n = float(n) # Конвертируем аргумент в тип float
    except ValueError:
        print("Ошибка: введите число биткоинов в качестве аргумента")
        sys.exit(1)

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        usd_rate = data["bpi"]["USD"]["rate_float"] # Получаем текущую цену биткоина в долларах
        total_price = n * usd_rate
        print(f"Текущая цена {n} биткоинов в долларах США: {total_price:,.4f}")
    except requests.RequestException:
        print("Аргумент командной строки не число")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пропущен аргумент командной строки")
        sys.exit(1)

    get_bitcoin_price(sys.argv[1])
