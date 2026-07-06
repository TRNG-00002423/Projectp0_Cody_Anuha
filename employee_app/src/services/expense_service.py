from models.expense import Expense
from repositories.expense_repository import ExpenseRepository
from repositories.approval_repository import ApprovalRepository
from enums.status_enum import Status
from exceptions.status_not_pending_exception import StatusNotPendingException

class ExpenseService:
    def get_expenses_from_user_id(self ,user_id : int):
        er = ExpenseRepository()
        return er.get_expenses_from_user_id(user_id)
    
    def add_or_update_expense(self, expense : Expense):
        er = ExpenseRepository()
        return er.add_or_update_expense(expense)
    
    def delete_pending_expense(self, expense : Expense):
        er = ExpenseRepository()
        ar = ApprovalRepository()
        
        approval = ar.get_approval_from_expense_id(expense.id)
        
        if approval.status == Status.PENDING:
            er.delete_expense(expense)
        else:
            raise StatusNotPendingException("Cannot delete expense; status is not pending.")
            
        