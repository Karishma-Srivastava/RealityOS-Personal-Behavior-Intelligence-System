# backend/db.py

import sqlite3

def get_connection():
    return sqlite3.connect("realityos.db")



def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        avg_productivity REAL,
        avg_study REAL,
        avg_sleep REAL
    )
    """)

    conn.commit()
    conn.close()

def save_metrics(metrics):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO results (avg_productivity, avg_study, avg_sleep)
    VALUES (?, ?, ?)
    """, (
        metrics["avg_productivity"],
        metrics["avg_study_hours"],
        metrics["avg_sleep_hours"]
    ))

    conn.commit()
    conn.close()