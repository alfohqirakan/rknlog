# database.py
import sqlite3
import traceback
import hashlib

# الاتصال بقاعدة البيانات
conn = sqlite3.connect('raakanbot.db', check_same_thread=False)
cursor = conn.cursor()

# إنشاء جدول تخزين الطلبات
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    language TEXT DEFAULT 'unknown',
    request TEXT NOT NULL,
    generated_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# إنشاء جدول المسؤولين
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()

# حفظ طلب المستخدم
def save_request(user_id, language, request, generated_code):
    try:
        if not user_id or not request:
            raise ValueError("🚫 Missing required fields: user_id or request")

        cursor.execute('''
            INSERT INTO user_requests (user_id, language, request, generated_code)
            VALUES (?, ?, ?, ?)
        ''', (
            user_id.strip()[:100],
            language.strip().lower()[:20] if language else 'unknown',
            request.strip(),
            generated_code.strip() if generated_code else None
        ))

        conn.commit()
        print("✅ Request saved successfully.")

    except sqlite3.IntegrityError as e:
        print("⚠️ Database integrity error:", e)
    except Exception as e:
        print("❌ Unexpected error saving request:")
        traceback.print_exc()

# إنشاء مسؤول
def create_admin(username, password):
    try:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO admin_users (username, password_hash)
            VALUES (?, ?)
        ''', (username, password_hash))
        conn.commit()
        print(f"✅ Admin '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"⚠️ Admin '{username}' already exists.")
    except Exception:
        traceback.print_exc()

# التحقق من دخول المسؤول
def verify_admin(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('SELECT * FROM admin_users WHERE username = ? AND password_hash = ?', (username, password_hash))
    return cursor.fetchone() is not None