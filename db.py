import sqlite3, json
from datetime import datetime

DB = "travel.db"

def get_conn():
    return sqlite3.connect(DB, check_same_thread=False)

def init_db():
    conn = get_conn()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS trips(
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        travel_data TEXT,
        itinerary TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_trip(data, itinerary):
    conn = get_conn()
    conn.execute("""
        INSERT INTO trips(timestamp, travel_data, itinerary)
        VALUES (?, ?, ?)
    """, (
        datetime.now().isoformat(),
        json.dumps(data),
        itinerary
    ))
    conn.commit()
    conn.close()

def load_trips(limit=20):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM trips ORDER BY id DESC LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "timestamp": r[1],
            "travel_data": json.loads(r[2]),
            "itinerary": r[3]
        }
        for r in rows
    ]