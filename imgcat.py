import sys
from PIL import Image
from asciimatics.screen import Screen

def print_ascii_art(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert('L')  # Преобразуем в градации серого
        img.thumbnail((80, 40))  # Изменяем размер для терминала, сохраняя пропорции

        # Проверяем, что изображение не пустое
        if img.size[0] == 0 or img.size[1] == 0:
            print("Ошибка: изображение имеет нулевой размер.")
            return

        pixels = img.getdata()
        ascii_chars = "@%#*+=-:. "
        
        # Проверяем, что все пиксели находятся в допустимом диапазоне
        ascii_str = ''
        for pixel in pixels:
            if pixel < 0 or pixel > 255:
                print(f"Ошибка: недопустимое значение пикселя {pixel}.")
                return
            index = min(pixel // 25, len(ascii_chars) - 1)  # Исправлено
            ascii_str += ascii_chars[index]

        # Проверяем, что ascii_str не пустой
        if not ascii_str:
            print("Ошибка: не удалось создать ASCII-арт из изображения.")
            return

        # Проверяем, что длина строки не превышает ширину изображения
        ascii_art = [ascii_str[index: index + img.width] for index in range(0, len(ascii_str), img.width)]

        screen = Screen.open()
        screen.clear_buffer(7, 0, 0)
        for i, line in enumerate(ascii_art):
            screen.print_at(line, 0, i)
        screen.refresh()
        screen.wait_for_input(10)
    except Exception as e:
        print(f"Ошибка: {e}")

def print_image_info(image_path):
    try:
        img = Image.open(image_path)
        info = img.info
        print(f"Метаданные изображения {image_path}:")
        for key, value in info.items():
            print(f"{key}: {value}")
        print(f"Размер: {img.size} пикселей")
        print(f"Формат: {img.format}")
        
        # Проверка формата
        if img.format not in ['JPEG', 'JPG', 'PNG', 'GIF']:
            print("Предупреждение: формат изображения не поддерживается для ASCII-арта.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: imgcat cat <путь_к_изображению> | imgcat info <путь_к_изображению>")
        print("Версия программы 1.0.5, Распространяется под лицензией GNU GPL v3.0")
        sys.exit(1)

    command = sys.argv[1]
    image_path = sys.argv[2]

    if command == "cat":
        print_ascii_art(image_path)
    elif command == "info":
        print_image_info(image_path)
    else:
        print("Неизвестная команда. Используйте 'cat' или 'info'.")
