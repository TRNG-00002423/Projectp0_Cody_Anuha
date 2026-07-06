from ui.menu.menu import Menu
from ui.helper.menu_helper import MenuHelper
from models.user import User
from services.approval_service import ApprovalService
from services.expense_service import ExpenseService
from models.expense import Expense
from models.approval import Approval
from enums.status_enum import Status

class PendingSubmissionMenu(Menu):
    mh : MenuHelper
    user : User
    window_opened = False
    
    def __init__(self, user : User):
        self.mh = MenuHelper()
        self.user = user
    
    def open(self):
        self.window_opened = True
        
        while(self.window_opened):
            self.mh.display_header_2_with_menu("Pending Submission Menu", f"Make your selection.")
            self.mh.display_numbered_list(["View Pending Submissions", "Edit Pending Submission", "Delete Pending Submission", "Exit"])
            selection = input()
            
            match selection:
                case "1":
                    self._view_pending_submissions()
                case "2":
                    self._edit_pending_submission()
                case "3":
                    self._delete_pending_submission()
                case "4":
                    self._exit()
                case _:
                    print("Unknown command.")
    
    
    def _view_pending_submissions(self):
        self.mh.display_header_2("Pending Submissions")
        self._show_and_return_pending_submissions()
    
    def _show_and_return_pending_submissions(self):
        aps = ApprovalService()
        es = ExpenseService()
        
        approvals = aps.get_all_approvals_from_user_id(self.user.id)
        approvals_pending = list(filter(lambda x: x.status == Status.PENDING, approvals))
        expenses = es.get_expenses_from_user_id(self.user.id)
        
        expense_lookup = {expense.id: expense for expense in expenses}

        pairs = list(
            map(
                lambda approval: (approval, expense_lookup[approval.expense_id]),
                approvals_pending
            )
        )
        
        flipped_pairs = list(map(lambda pair: (pair[1], pair[0]), pairs))
        
        self.mh.display_paired_numbered_list(flipped_pairs)
        return flipped_pairs
    
    def _edit_pending_submission(self):
        self.mh.display_header_2_with_menu("EDIT EXPENSE", "Make your selection.")
        pairs = self._show_and_return_pending_submissions()
        expense : Expense = None
        
        while expense == None:
            try:
                selection = int(input())
                expense = pairs[selection-1][0]
            except ValueError:
                print("Invalid selection")
        
        self.mh.display_header_2("Enter updated expense information")
        
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
            except IndexError:
                print("Invalid selection")
        
        # get description
        description : str = None
        while description == None:
            temp : str = input("Description (cannot be empty): ")
            if len(temp) > 0:
                description = temp
            else:
                print("Invalid description")
        
        expense.amount = amount
        expense.description = description
        es = ExpenseService()
        es.add_or_update_expense(expense)
    
    def _delete_pending_submission(self):
        self.mh.display_header_2_with_menu("DELETE EXPENSE", "Make your selection.")
        pairs = self._show_and_return_pending_submissions()
        expense : Expense = None
        
        while expense == None:
            try:
                selection = int(input())
                expense = pairs[selection-1][0]
            except ValueError:
                print("Invalid selection")
            except IndexError:
                print("Invalid selection")
        
        es = ExpenseService()
        es.delete_pending_expense(expense)
    
    
    def _exit(self):
        self.window_opened = False