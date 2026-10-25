import requests

SUPPORTED_CURRENCIES = ["USD", "EUR", "PLN"]
NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


def get_nbu_rates() -> dict[str, float] | None:
    try:
        response = requests.get(NBU_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        rates = {}
        for item in data:
            code = item.get("cc")
            if code in SUPPORTED_CURRENCIES:
                rates[code] = item.get("rate")
        return rates

    except requests.exceptions.RequestException as e:
        print(f"Помилка з'єднання з API НБУ: {e}")
        return None
    except ValueError:
        print("Помилка обробки відповіді від сервера.")
        return None


def get_user_currency() -> str:
    currencies_str = ", ".join(SUPPORTED_CURRENCIES)
    while True:
        currency = (
            input(f"Оберіть валюту ({currencies_str}): ").strip().upper()
        )
        if currency in SUPPORTED_CURRENCIES:
            return currency
        print(f"Непідтримувана валюта! Доступні варіанти: {currencies_str}")


def get_amount() -> float:
    while True:
        raw_amount = input("Введіть суму: ").strip().replace(",", ".")
        try:
            amount = float(raw_amount)
            if amount < 0:
                print("Сума не може бути від'ємною!")
                continue
            return amount
        except ValueError:
            print("Помилка: введіть коректне числове значення.")


def main():
    print("\n=== Конвертер валют за курсом НБУ ===")
    rates = get_nbu_rates()
    if not rates:
        print("Не вдалося завантажити курси валют. Роботу програми завершено.")
        return

    currency = get_user_currency()
    amount = get_amount()

    rate = rates.get(currency)
    converted_amount = amount * rate

    print("\n--- Результат ---")
    print(f"Курс {currency}: {rate:.4f} UAH")
    print(f"{amount:.2f} {currency} = {converted_amount:.2f} UAH")


if __name__ == "__main__":
    main()