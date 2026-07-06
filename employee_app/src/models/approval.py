from enums.status_enum import Status
from datetime import datetime
from exceptions.invalid_status_exception import InvalidStatusException

class Approval:
    id : int
    expense_id : int
    status : Status
    reviewer_id : int | None
    comment : str | None
    review_date : datetime | None
    
    def __init__(self, id : int, expense_id : int, status : Status, reviewer_id : int = None, comment : str = None, review_date : datetime = None):
        self.id = id
        self.expense_id = expense_id
        self.status = status
        self.reviewer_id = reviewer_id
        self.comment = comment
        self.review_date = review_date
    
    @classmethod
    def raw_to_approval(cls, id : int, expense_id : int, status : str, reviewer_id : int = None, comment : str = None, review_date : str = None):
        if review_date != None:
            review_date = datetime.fromisoformat(review_date)
        
        if status == "APPROVED":
            status = Status.APPROVED
        elif status == "DENIED":
            status = Status.DENIED
        elif status == "PENDING":
            status = Status.PENDING
        else:
            raise InvalidStatusException("Status must be 'APPROVED', 'PENDING', or 'DENIED'")
            
        return cls(id, expense_id, status, reviewer_id, comment, review_date)

    def __str__(self):
        if self.status == Status.PENDING:
            return f"Approval ID {self.id} of Expense ID {self.expense_id}:\n - Status: {self.status.name}"
        else:
            return f"Approval ID {self.id} of Expense ID {self.expense_id}:\n - Status: {self.status.name}\n - Reviewer ID {self.reviewer_id} commented: {self.comment}\n - Date: {self.review_date.strftime("%d/%m/%Y, %H:%M:%S")}"