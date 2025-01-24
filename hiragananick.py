import random

# Списки слогов хираганы
hiragana_syllables = [
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の",
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ",
    "ら", "り", "る", "れ", "ろ",
    "わ", "を", "ん"
]

# Генерация никнейма
def generate_nickname(length=5):
    nickname = ''.join(random.choice(hiragana_syllables) for _ in range(length))
    return nickname

# Пример использования
if __name__ == "__main__":
    for _ in range(5):  # Генерируем 5 никнеймов
        print(generate_nickname())

