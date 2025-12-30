import sqlite3
from app.core.feedback_schema import FeedbackInput

DB_PATH = "app/data/feedback.db"

def init_feedback_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint_text TEXT,
            predicted_department TEXT,
            corrected_department TEXT,
            predicted_priority TEXT,
            corrected_priority TEXT,
            reviewer_role TEXT,
            feedback_time TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_feedback(feedback: FeedbackInput):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO feedback (
            complaint_text,
            predicted_department,
            corrected_department,
            predicted_priority,
            corrected_priority,
            reviewer_role,
            feedback_time
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        feedback.complaint_text,
        feedback.predicted_department,
        feedback.corrected_department,
        feedback.predicted_priority,
        feedback.corrected_priority,
        feedback.reviewer_role,
        feedback.feedback_time.isoformat()
    ))
    conn.commit()
    conn.close()
