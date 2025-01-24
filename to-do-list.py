def display_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []
    
    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Просмотреть задачи")
        print("4. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            task = input("Введите задачу: ")
            tasks.append(task)
            print(f"Задача '{task}' добавлена.")
        
        elif choice == '2':
            display_tasks(tasks)
            task_index = int(input("Введите номер задачи для удаления: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Задача '{removed_task}' удалена.")
            else:
                print("Неверный номер задачи.")
        
        elif choice == '3':
            display_tasks(tasks)
        
        elif choice == '4':
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()

