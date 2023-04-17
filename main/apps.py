from django.apps import AppConfig
import sqlite3

class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='post';")
        table_exists = cursor.fetchone() is not None
        if not table_exists:
            conn.execute('''CREATE TABLE post
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        userid INTEGER NOT NULL,
                        content TEXT NOT NULL,
                        datetime TEXT NOT NULL);''')
            conn.commit()
            
        conn.close()