import sqlite3
from sqlite3 import Error

# تعریف کلاس diba
class diba:
    def __init__(self):
        self.data=None
        con=self.create_connection()  # ایجاد اتصال به دیتابیس
        self.create_table(con)  # ایجاد جدول در دیتابیس
    
    # تابع ایجاد اتصال به دیتابیس
    def create_connection(self):
        conn = None;
        try:
            conn = sqlite3.connect('db_name.db')  # اتصال به دیتابیس db_name.db
        except Error as e:
            pass
        return conn

    # تابع ایجاد جدول در دیتابیس
    def create_table(self,conn):
        try:
            c = conn.cursor()  # ایجاد یک کرسر

            # اجرای دستور SQL برای ایجاد جدول
            c.execute('''
                CREATE TABLE IF NOT EXISTS table_name (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    link TEXT NOT NULL
                )
            ''')
            conn.commit()  # ذخیره تغییرات
        except Error as e:
            pass

    # تابع انتخاب لینک ها از دیتابیس
    def seletor(self):
        try:
            con = sqlite3.connect('db_name.db')  # اتصال به دیتابیس
            cur = con.cursor()  # ایجاد یک کرسر
            cur.execute('SELECT link FROM table_name')  # اجرای دستور SQL برای انتخاب لینک ها
            links = cur.fetchall()  # دریافت تمام نتایج
            con.close()  # بستن اتصال به دیتابیس
        except Exception as e:
            pass
        return links  # برگرداندن لینک ها
        
    # تابع درج داده در دیتابیس
    def inserter(self,data):
        try:
            self.data=data  # ذخیره داده
            con = sqlite3.connect('db_name.db')  # اتصال به دیتابیس
            cur = con.cursor()  # ایجاد یک کرسر
            # اجرای دستور SQL برای درج داده
            cur.execute('INSERT OR IGNORE INTO table_name (link) VALUES (?)', (self.data,))
            con.commit()  # ذخیره تغییرات
            con.close()  # بستن اتصال به دیتابیس
        except Exception as e:
            pass

    # تابع حذف داده از دیتابیس
    def deleter (self):
        try:
            con=sqlite3.connect('db_name.db')  # اتصال به دیتابیس
            cur=con.cursor()  # ایجاد یک کرسر
            # اجرای دستور SQL برای انتخاب شناسه
            cur.execute("SELECT id FROM table_name ORDER BY id ASC LIMIT 1 OFFSET 29")
            row = cur.fetchone()  # دریافت نتیجه
            if row is not None:
                id_10th = row[0]
            # اجرای دستور SQL برای حذف داده
            cur.execute("DELETE FROM table_name WHERE id <= ?", (id_10th,))

            con.commit()  # ذخیره تغییرات
            con.close()  # بستن اتصال به دیتابیس
            print("Data Base get lighter :)")  # چاپ پیام
        except Exception as e:
            pass
