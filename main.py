# main.py
from database import conn, cursor
import traceback

# تهيئة قاعدة البيانات (مثال)
def init_db():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                role TEXT DEFAULT 'user'
            )
        ''')
        conn.commit()
        print("✅ تم إنشاء الجدول بنجاح.")
    except Exception as e:
        print("❌ خطأ:", traceback.format_exc())

# نقطة التشغيل الرئيسية
if __name__ == '__main__':
    print("🔄 بدء تشغيل راكان بوت...")
    init_db()
    print("🚀 النظام جاهز.")