from enums.status_enum import Status
from models.approval import Approval
from database.database import get_connection
from exceptions.not_found_exception import NotFoundException
from repositories.expense_repository import ExpenseRepository
from datetime import datetime

class ApprovalRepository:
    def get_approval_from_id(self, id : int):
        db_con = get_connection()
        db_cur = db_con.cursor()
        
        db_cur.execute("SELECT * FROM approvals WHERE id = ?", (id,))
        
        raw_approval_data = db_cur.fetchone()
        
        if raw_approval_data == None:
            raise NotFoundException("Approval ID does not exist.")
        
        db_con.close()
        return Approval.raw_to_approval(raw_approval_data[0], raw_approval_data[1], raw_approval_data[2],
                                               raw_approval_data[3], raw_approval_data[4], raw_approval_data[5])
    
    def get_approval_from_expense_id(self, expense_id : int):
        db_con = get_connection()
        db_cur = db_con.cursor()
        
        db_cur.execute("SELECT * FROM approvals WHERE expense_id = ?", (expense_id,))
        
        raw_approval_data = db_cur.fetchone()
        
        if raw_approval_data == None:
            raise NotFoundException("Expense ID does not exist.")
        
        db_con.close()
        return Approval.raw_to_approval(raw_approval_data[0], raw_approval_data[1], raw_approval_data[2],
                                               raw_approval_data[3], raw_approval_data[4], raw_approval_data[5])
    
    def get_all_approvals_from_user_id(self, user_id : int):
        
        er = ExpenseRepository()
        user_expenses = er.get_expenses_from_user_id(user_id)
        
        user_approvals = []
        
        for expense in user_expenses:
            try:
                approval = self.get_approval_from_expense_id(expense.id)
                user_approvals.append(approval)
            except NotFoundException:
                pass # WARN
            
        return user_approvals
    
    def add_or_update_approval(self, approval : Approval):
        db_con = get_connection()
        db_cur = db_con.cursor()
        
        db_cur.execute("SELECT * FROM approvals WHERE id = ?", (approval.id,))
        
        raw_approval_data = db_cur.fetchone()
        
        if raw_approval_data == None:
            # add
            db_cur.execute("INSERT INTO approvals (expense_id, status, reviewer_id, comment, review_date) VALUES (?, ?, ?, ?, ?)", 
                   (approval.expense_id, approval.status.name, approval.reviewer_id, approval.comment, None))
        else:
            # update
            db_cur.execute("UPDATE approvals SET expense_id = ?, status = ?, reviewer_id = ?, comment = ?, review_date = ? WHERE id = ?", 
                           (approval.expense_id, approval.status.name, approval.reviewer_id, approval.comment, datetime.isoformat(approval.review_date)))
        
        db_con.commit()
        db_con.close()