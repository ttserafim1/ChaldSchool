import sqlite3
import os

# Путь к базе данных
DATABASE_PATH = 'chaldschool.db'

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Для удобства работы с результатами
    return conn

# Функция для создания таблицы пользователей
def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Создание таблицы, если она ещё не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

# Функция для добавления пользователя
def add_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Добавляем нового пользователя
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print(f"Пользователь {username} успешно добавлен!")
    except sqlite3.IntegrityError:
        print(f"Ошибка: Пользователь с именем {username} уже существует!")
    finally:
        conn.close()

# Функция для проверки пользователя
def check_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        print(f"Добро пожаловать, {username}!")
        return True
    else:
        print("Неверный логин или пароль!")
        return False

# Пример работы с функциями
if __name__ == '__main__':
    # Создаем таблицу, если её нет
    create_users_table()

    # Добавляем пользователей (если нужно)
    add_user('tt_serafim_1', 'cat201376')

    # Пробуем проверить логин и пароль
    check_user('tt_serafim_1', 'cat201376')
