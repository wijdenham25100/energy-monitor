import sqlite3
from datetime import datetime

DB_PATH = "energy.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS readings (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                depot     TEXT    NOT NULL,
                type      TEXT    NOT NULL CHECK(type IN ('Strom', 'Gas')),
                value_kwh REAL    NOT NULL,
                date      TEXT    NOT NULL
            )
        """)
        conn.commit()

def insert_reading(depot, type_, value_kwh, date):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO readings (depot, type, value_kwh, date) VALUES (?, ?, ?, ?)",
            (depot, type_, value_kwh, date)
        )
        conn.commit()

def get_all_readings():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, depot, type, value_kwh, date FROM readings ORDER BY date DESC"
        ).fetchall()
    return rows

def delete_reading(id_):
    with get_connection() as conn:
        conn.execute("DELETE FROM readings WHERE id = ?", (id_,))
        conn.commit()

def seed_data():
    """Beispieldaten einfügen falls Tabelle leer."""
    with get_connection() as conn:
        count = conn.execute("SELECT COUNT(*) FROM readings").fetchone()[0]
    if count > 0:
        return

    import random
    depots = ["Berlin", "Hamburg", "Dortmund", "Frankfurt", "München"]
    for depot in depots:
        for month in range(1, 7):
            date = f"2026-{month:02d}-01"
            insert_reading(depot, "Strom", round(random.uniform(200, 600), 1), date)
            insert_reading(depot, "Gas",   round(random.uniform(100, 400), 1), date)