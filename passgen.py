import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase  # всегда добавляем строчные буквы

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("Должен быть выбран хотя бы один тип символов.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Добро пожаловать в генератор паролей!")

    while True:
        try:
            length = int(input("Введите длину пароля (минимум 1): "))
            if length < 1:
                print("Длина пароля должна быть хотя бы 1.")
                continue

            use_uppercase = input("Включить заглавные буквы? (y/n): ").lower() == 'y'
            use_numbers = input("Включить цифры? (y/n): ").lower() == 'y'
            use_special = input("Включить специальные символы? (y/n): ").lower() == 'y'

            password = generate_password(length, use_uppercase, use_numbers, use_special)
            print(f"Сгенерированный пароль: {password}")

            if input("Хотите сгенерировать еще один пароль? (y/n): ").lower() != 'y':
                break

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()

