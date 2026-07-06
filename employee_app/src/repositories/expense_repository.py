from models.expense import Expense
from database.database import get_connection
from exceptions.not_found_exception import NotFoundException
from datetime import datetime

class ExpenseRepository:
    def get_expense_from_id(self, id : int):
        db_con = get_connection()
        db_cur = db_con.cursor()
        
        db_cur.execute("SELECT * FROM expenses WHERE id = ?", (id,))
        
        raw_expense_data = db_cur.fetchone()
        
        if raw_expense_data == None:
            raise NotFoundException("Expense ID does not exist.")
        
        db_con.close()
        return Expense.from_date_iso_8601_str(raw_expense_data[0], raw_expense_data[1], raw_expense_data[2], 
                                              raw_expense_data[3], raw_expense_data[4])
    
    def get_expenses_from_user_id(self, user_id : int):
        db_con = get_connection()
        db_cur = db_con.cursor()
        
        db_cur.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id,))
        
        raw_expense_data_ls = db_cur.fetchall()
        
        if len(raw_expense_data_ls) == 0:
            raise NotFoundException("Expense ID does not exist.")
        
        expenses = []
        
        for raw_expense_data in raw_expense_data_ls:
            expenses.append(Expense.from_date_iso_8601_str(raw_expense_data[0], raw_expense_data[1], raw_expense_data[2], 
                                              raw_expense_data[3], raw_expense_data[4]))
        
        db_con.close()
        return expenses
    
    def add_or_update_expense(self, expense : Expense):
        db_con = get_connection()
        db_cur = db_con.cursor()
        
        db_cur.execute("SELECT * FROM expenses WHERE id = ?", (expense.id,))
        
        raw_expense_data = db_cur.fetchone()
        
        if raw_expense_data == None:
            # add
            db_cur.execute("INSERT INTO expenses (user_id, amount, description, date) VALUES (?, ?, ?, ?)", 
                   (expense.user_id, expense.amount, expense.description, datetime.isoformat(expense.date)))
        else:
            # update
            db_cur.execute("UPDATE expenses SET user_id = ?, amount = ?, description = ?, date = ? WHERE id = ?", 
                           (expense.user_id, expense.amount, expense.description, datetime.isoformat(expense.date), expense.id))
        
        db_con.commit()
        db_con.close()
    
    def delete_expense(self, expense : Expense):
        db_con = get_connection()
        db_cur = db_con.cursor()
        
        db_cur.execute("SELECT * FROM expenses WHERE id = ?", (expense.id,))
        
        raw_expense_data = db_cur.fetchone()
        
        if raw_expense_data == None:
            raise NotFoundException("Expense ID does not exist.")
        
        db_cur.execute("DELETE FROM expenses WHERE id = ?", (expense.id,))
        
        db_con.commit()
        db_con.close()
    