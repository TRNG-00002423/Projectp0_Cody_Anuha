from database.database import init_db
from ui.menu.login_menu import LoginMenu

if __name__ == "__main__":
    init_db()
    
    lm = LoginMenu()
    lm.open()