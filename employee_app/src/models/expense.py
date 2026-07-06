from datetime import datetime

class Expense:
    id : int
    user_id : int
    amount : float
    description : str
    date : datetime
    def __init__(self, id : int, user_id : int, amount : float, description : str, date : datetime):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.description = description
        self.date = date
    
    @classmethod
    def from_date_iso_8601_str(cls, id : int, user_id : int, amount : float, description : str, date : str):
        date = datetime.fromisoformat(date)
        return cls(id, user_id, amount, description, date)

    def __str__(self):
        return f"Expense ID {self.id} from User ID {self.user_id}\n - Description: '{self.description}'\n - Amount: ${self.amount}\n - Date: {self.date.strftime("%d/%m/%Y, %H:%M:%S")}"