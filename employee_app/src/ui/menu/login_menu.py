from ui.menu.menu import Menu
from ui.helper.menu_helper import MenuHelper
from services.login_service import LoginService
from models.user import User
from ui.menu.main_menu import MainMenu

class LoginMenu(Menu):
    on_startup = True
    
    mh : MenuHelper
    window_opened = False
    
    def __init__(self):
        self.mh = MenuHelper()
    
    def open(self):
        self.window_opened = True
        
        if LoginMenu.on_startup:
            LoginMenu.on_startup = False
            self.mh.display_header_1("Welcome!")
        
        while(self.window_opened):
            self.mh.display_header_2_with_menu("Login Menu", "Please make a selection")
            self.mh.display_numbered_list(["Login", "Exit"])
            selection = input()
            
            match selection:
                case "1":
                    self._attempt_login()
                case "2":
                    self._exit()
                case _:
                    print("Unknown command.")
    
    
    def _attempt_login(self):
        self.mh.display_header_2("Please enter employee username and password.")
        username = input("Username: ")
        password = input("Password: ")
        
        
        ls = LoginService()
        usr = ls.attempt_login(username, password)
        
        if isinstance(usr, User):
            print("Login Successful!")
            mm = MainMenu(usr)
            mm.open()
    
    
    def _exit(self):
        self.window_opened = False