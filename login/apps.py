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
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL);''')
            print("User table created")
            
        conn.close()
