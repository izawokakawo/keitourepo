def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount
    return amount * rates[from_currency][to_currency]

def main():
    # Фиксированные курсы валют (пример)
    rates = {
        'USD': {'EUR': 0.85, 'RUB': 74.0, 'USD': 1.0},
        'EUR': {'USD': 1.18, 'RUB': 87.0, 'EUR': 1.0},
        'RUB': {'USD': 0.013, 'EUR': 0.011, 'RUB': 1.0}
    }

    print("Добро пожаловать в конвертер валют!")
    print("Доступные валюты: USD, EUR, RUB")

    while True:
        from_currency = input("Введите валюту, из которой хотите конвертировать (или 'q' для выхода): ").upper()
        if from_currency == 'Q':
            print("Выход из программы.")
            break

        if from_currency not in rates:
            print("Неверная валюта. Пожалуйста, попробуйте снова.")
            continue

        to_currency = input("Введите валюту, в которую хотите конвертировать: ").upper()
        if to_currency not in rates[from_currency]:
            print("Неверная валюта. Пожалуйста, попробуйте снова.")
            continue

        try:
            amount = float(input("Введите сумму для конвертации: "))
            converted_amount = convert_currency(amount, from_currency, to_currency, rates)
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    main()

