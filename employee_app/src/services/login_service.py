from repositories.user_repository import UserRepository
from exceptions.failed_login_exception import FailedLoginException

class LoginService:
    def attempt_login(self, username : str, password : str):
        ur = UserRepository()
        usr = None
        
        try:
            usr = ur.get_user_from_login_info(username, password)
        except FailedLoginException as e:
            print(e.message)
        
        return usr
        