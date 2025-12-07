# main.py

# Импортируем модули для работы с переменными окружения
import os
from dotenv import load_dotenv

# 1. Загрузка переменных из .env-файла в окружение программы
load_dotenv()

# 4. & 5. Функция, которая читает переменную AUTHOR
def print_author():
    # os.getenv("AUTHOR") читает значение из окружения,
    # которое было загружено из файла .env
    author = os.getenv("AUTHOR") 
    
    # Печатаем результат
    print(f"Автор проекта: {author}")

# 6. Проверяем работу функции: вызываем ее
print_author()
