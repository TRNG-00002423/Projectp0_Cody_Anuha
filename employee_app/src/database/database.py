from pathlib import Path
import sqlite3
import os

BASE_DIR = Path(__file__).resolve().parents[3]

DB_PATH = BASE_DIR / "database" / "database.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"

def get_connection():
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")
    con.commit()
    return con

def init_db():
    db_exists = os.path.exists(DB_PATH)
    
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    
    if not db_exists:
        with open(SCHEMA_PATH, "r") as f:
            schema_sql = f.read()
        
        cur.executescript(schema_sql)
        con.commit()
        
    con.close()
        
        