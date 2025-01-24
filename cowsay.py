import random

def cowsay(message):
    cow_faces = [
        r"        ^__^",
        r"        (oo)\_______",
        r"        (__)\       )\/\\",
        r"            ||----w |",
        r"            ||     ||"
    ]
    
    # Создаем "речевой пузырь"
    bubble = create_bubble(message)
    
    # Выводим пузырь и корову
    print(bubble)
    print("\n".join(cow_faces))

def create_bubble(message):
    # Определяем ширину пузыря
    width = len(message) + 2
    bubble_top = " " + "_" * width
    bubble_bottom = " " + "-" * width
    bubble_message = f"< {message} >"
    
    return f"{bubble_top}\n{bubble_message}\n{bubble_bottom}"

if __name__ == "__main__":
    user_input = input("Введите сообщение для коровы: ")
    cowsay(user_input)

