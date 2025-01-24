import os
import requests
import argparse

REPO_URL = "https://raw.githubusercontent.com/izawokakawo/keitourepo/main"  # URL для доступа к файлам
TARGET_DIRECTORY = "KeitouOSDirectory/usr"

def ensure_target_directory():
    """Создает целевую директорию, если она не существует."""
    os.makedirs(TARGET_DIRECTORY, exist_ok=True)

def download_package(package_name):
    target_path = os.path.join(TARGET_DIRECTORY, f"{package_name}.py")
    
    # Удаляем старую версию, если она существует
    if os.path.exists(target_path):
        os.remove(target_path)
    
    # Формируем URL для загрузки файла
    file_url = f"{REPO_URL}/{package_name}.py"
    
    try:
        response = requests.get(file_url)
        response.raise_for_status()  # Проверяем, что запрос успешен
        
        # Сохраняем файл в целевую директорию
        with open(target_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Пакет {package_name} успешно установлен.")
    except requests.HTTPError:
        print(f"Пакет {package_name} не найден в репозитории.")
    except Exception as e:
        print(f"Произошла ошибка при загрузке пакета: {e}")

def update_package(package_name):
    target_path = os.path.join(TARGET_DIRECTORY, f"{package_name}.py")
    
    if os.path.exists(target_path):
        download_package(package_name)  # Просто перезагружаем файл
    else:
        print(f"Пакет {package_name} не установлен. Установите его с помощью команды 'kitkat install {package_name}'.")

def main():
    ensure_target_directory()  # Убедимся, что целевая директория существует

    parser = argparse.ArgumentParser(description='Пакетный менеджер KitKat для KeitouOS')
    parser.add_argument('command', choices=['install', 'update'], help='Команда для выполнения')
    parser.add_argument('package', help='Имя пакета (без .py)')

    args = parser.parse_args()

    if args.command == 'install':
        download_package(args.package)
    elif args.command == 'update':
        update_package(args.package)

if __name__ == "__main__":
    main()
