# bot_core.py
from database import cursor, conn
import traceback

# دالة إضافة مستخدم
def add_user(username, role='user'):
    try:
        cursor.execute("INSERT INTO users (username, role) VALUES (?, ?)", (username, role))
        conn.commit()
        print(f"✅ تم إضافة المستخدم: {username}")
    except Exception as e:
        print("❌ خطأ أثناء الإضافة:", traceback.format_exc())

# دالة عرض المستخدمين
def list_users():
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print("📋 قائمة المستخدمين:")
        for u in users:
            print(f"- ID: {u[0]}, Username: {u[1]}, Role: {u[2]}")
    except Exception as e:
        print("❌ خطأ أثناء القراءة:", traceback.format_exc())

# تجربة التشغيل
if __name__ == '__main__':
    add_user("raakan_admin", "owner")
    list_users()