import sqlite3
from os import getenv
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class ConnectDB:
    def __init__(self):
        self.db_path = getenv("DB_SQL")
        self.conn = sqlite3.connect(self.db_path, timeout=10)
        self.cursor = self.conn.cursor()
        self.check_create_table()

    def __del__(self):
        self.close()

    def check_create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                title TEXT UNIQUE,
                meta TEXT,
                description TEXT,
                link TEXT
            )
        ''')
        self.conn.commit()
        logging.info("تم إنشاء الجدول أو التحقق منه")

    def check_field_in_db(self, item):
        self.cursor.execute('SELECT 1 FROM projects WHERE title = ?', (item['title'],))
        return self.cursor.fetchone() is not None

    def insert_in_db(self, item):
        if self.check_field_in_db(item):
            logging.warning(f"المشروع موجود بالفعل:🔁 {item['title']}")
            return False
        self.cursor.execute('''
            INSERT INTO projects (title, meta, description, link)
            VALUES (?, ?, ?, ?)
        ''', (item['title'], item['meta'], item['description'], item['link']))
        self.conn.commit()
        logging.info(f"تم حفظ المشروع:✅ {item['title']}")
        return True

    def close(self):
        self.conn.close()
