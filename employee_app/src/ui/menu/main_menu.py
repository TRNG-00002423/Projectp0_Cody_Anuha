from ui.menu.menu import Menu
from ui.helper.menu_helper import MenuHelper
from models.user import User
from ui.menu.pending_submission_menu import PendingSubmissionMenu
from models.expense import Expense
from datetime import datetime
from services.expense_service import ExpenseService
from services.approval_service import ApprovalService
from models.approval import Approval
from enums.status_enum import Status

class MainMenu(Menu):
    mh : MenuHelper
    user : User
    window_opened = False
    
    def __init__(self, user : User):
        self.mh = MenuHelper()
        self.user = user
    
    def open(self):
        self.window_opened = True
        
        while(self.window_opened):
            self.mh.display_header_2_with_menu("Main Menu", f"Hello, {self.user.username}!")
            self.mh.display_numbered_list(["Submit Expense", "View Expense History", "Open Pending Submission Menu", "Exit"])
            selection = input()
            
            match selection:
                case "1":
                    self._submit_expense()
                case "2":
                    self._view_expense_history()
                case "3":
                    self._open_pending_submission_menu()
                case "4":
                    self._exit()
                case _:
                    print("Unknown command.")
    
    
    def _submit_expense(self):
        self.mh.display_header_2("Enter expense information")
        
        # get amount
        amount : float = None
        while amount == None:
            try:
                temp : float = float(input("Amount (decimal value): "))
                if temp > 0:
                    amount = round(temp, 2)
                else:
                    print("Invalid amount")
            except ValueError:
                print("Invalid amount")
        
        # get description
        description : str = None
        while description == None:
            temp : str = input("Description (cannot be empty): ")
            if len(temp) > 0:
                description = temp
            else:
                print("Invalid description")
        
        e = Expense(-1, self.user.id, amount, description, datetime.now())
        es = ExpenseService()
        es.add_or_update_expense(e)
        aps = ApprovalService()
        latest_expense : Expense = es.get_expenses_from_user_id(self.user.id).pop()
        a = Approval(-1, latest_expense.id, Status.PENDING, None, None, None)
        aps.add_approval(a)
            
    
    def _view_expense_history(self):
        es = ExpenseService()
        aps = ApprovalService()
        
        approvals = aps.get_all_approvals_from_user_id(self.user.id)
        expenses = es.get_expenses_from_user_id(self.user.id)
        
        approval_lookup = {approval.expense_id: approval for approval in approvals}

        pairs = list(
            map(
                lambda expense: (expense, approval_lookup[expense.id]),
                expenses
            )
        )
        
        self.mh.display_header_2("Expense History")
        self.mh.display_paired_numbered_list(pairs)
    
    def _open_pending_submission_menu(self):
        psm = PendingSubmissionMenu(self.user)
        psm.open()
    
    
    def _exit(self):
        self.window_opened = False