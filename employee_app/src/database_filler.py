from database.database import get_connection, init_db
import bcrypt
from datetime import datetime

def fill_database():
    add_users()
    add_expenses()
    add_approvals()
    
    print("Database filled.")
    
def add_users():
    db_con = get_connection()
    db_cur = db_con.cursor()
    
    usr = "codykrause"
    psw = "123"
    psw_bytes = psw.encode('utf-8')
    salt = bcrypt.gensalt()
    psw_hash = bcrypt.hashpw(psw_bytes, salt)
    
    db_cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (usr, psw_hash, "EMPLOYEE"))
    db_con.commit()
    
    usr = "admin"
    psw = "password"
    psw_bytes = psw.encode('utf-8')
    salt = bcrypt.gensalt()
    psw_hash = bcrypt.hashpw(psw_bytes, salt)
    
    db_cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (usr, psw_hash, "MANAGER"))
    db_con.commit()
    
    db_con.close()

def add_expenses():
    db_con = get_connection()
    db_cur = db_con.cursor()
    
    db_cur.execute("INSERT INTO expenses (user_id, amount, description, date) VALUES (?, ?, ?, ?)", 
                   (1, 123.21, "Really yummy lunch.", datetime.isoformat(datetime.now())))
    db_con.commit()
    
    db_cur.execute("INSERT INTO expenses (user_id, amount, description, date) VALUES (?, ?, ?, ?)", 
                   (1, 87.54, "New keyboard.", datetime.isoformat(datetime.now())))
    db_con.commit()
    
    db_con.close()

def add_approvals():
    db_con = get_connection()
    db_cur = db_con.cursor()
    
    db_cur.execute("INSERT INTO approvals (expense_id, status, reviewer_id, comment, review_date) VALUES (?, ?, ?, ?, ?)",
                   (1, "APPROVED", 2, "Bring me back something.", datetime.isoformat(datetime.now())))
    db_con.commit()
    
    db_cur.execute("INSERT INTO approvals (expense_id, status) VALUES (?, ?)",
                   (2, "PENDING"))
    db_con.commit()
    
    db_con.close()

if __name__ == "__main__":
    init_db()
    fill_database()