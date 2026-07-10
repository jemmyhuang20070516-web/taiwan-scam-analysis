import os
import psycopg2
from dotenv import load_dotenv


# 讀取 .env
load_dotenv()

# PostgreSQL 連線字串
DATABASE_URL = os.getenv("DATABASE_URL")


# PostgreSQL 連線
def get_connection():
    return psycopg2.connect(DATABASE_URL)


# 建立資料表
def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS scam_cases (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            publish_date TEXT,
            content TEXT
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("PostgreSQL 資料表建立成功！")


# Create：新增資料
def insert_case(title, publish_date, content):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO scam_cases
        (title, publish_date, content)
        VALUES (%s, %s, %s)
    """, (
        title,
        publish_date,
        content
    ))

    conn.commit()
    cur.close()
    conn.close()

    print("新增資料成功！")


# Read：讀取全部資料
def get_all_cases():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, title, publish_date, content
        FROM scam_cases
        ORDER BY id DESC
    """)

    rows = cur.fetchall()

    cases = []

    for row in rows:
        cases.append({
            "id": row[0],
            "title": row[1],
            "publish_date": row[2],
            "content": row[3]
        })

    cur.close()
    conn.close()

    return cases


# Read：讀取單筆資料
def get_case_by_id(case_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, title, publish_date, content
        FROM scam_cases
        WHERE id = %s
    """, (case_id,))

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "publish_date": row[2],
        "content": row[3]
    }


# Update：修改資料
def update_case(case_id, title, publish_date, content):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE scam_cases
        SET title = %s,
            publish_date = %s,
            content = %s
        WHERE id = %s
    """, (
        title,
        publish_date,
        content,
        case_id
    ))

    conn.commit()
    cur.close()
    conn.close()

    print("修改資料成功！")


# Delete：刪除資料
def delete_case(case_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM scam_cases
        WHERE id = %s
    """, (case_id,))

    conn.commit()
    cur.close()
    conn.close()

    print("刪除資料成功！")


# 單獨執行 db.py 時建立資料表
if __name__ == "__main__":
    create_table()