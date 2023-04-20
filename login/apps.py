from django.apps import AppConfig
import sqlite3


class LoginConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "login"

    def ready(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user';")
        table_exists = cursor.fetchone() is not None
        if not table_exists:
            conn.execute('''CREATE TABLE user
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        account TEXT NOT NULL,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL);''')
            conn.execute("INSERT INTO user (account, name, email, password) VALUES (?, ?, ?, ?)", ('user1', '博物杂志', 'user1@example.com', 'password1'))
            conn.execute("INSERT INTO user (account, name, email, password) VALUES (?, ?, ?, ?)", ('user2', '中国国家地理', 'user2@example.com', 'password2'))
            conn.execute("INSERT INTO user (account, name, email, password) VALUES (?, ?, ?, ?)", ('user3', '历史研究院', 'user2@example.com', 'password3'))
            conn.commit()
            
        conn.close()
