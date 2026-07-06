from database.database import get_connection
import bcrypt
from models.user import User
from exceptions.failed_login_exception import FailedLoginException
from exceptions.not_found_exception import NotFoundException

class UserRepository:
    def get_user_from_id(self, id : int):
        db_con = get_connection()
        db_cur = db_con.cursor()
        db_cur.execute("SELECT * FROM users WHERE id = ?", (id,))
        
        raw_usr_data = db_cur.fetchone()
        
        if raw_usr_data == None:
            raise NotFoundException("User ID does not exist.")
        
        db_con.close()
        return User.from_str_role(raw_usr_data[0], raw_usr_data[1], raw_usr_data[3])
    
    def get_user_from_login_info(self, username : str, password : str):
        db_con = get_connection()
        db_cur = db_con.cursor()
        db_cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        
        raw_usr_data = db_cur.fetchone()
        
        if raw_usr_data == None:
            raise FailedLoginException("Username or password is incorrect.")
        
        psw_bytes = password.encode('utf-8')
        
        db_con.close()
        if bcrypt.checkpw(psw_bytes, raw_usr_data[2]):
            return User.from_str_role(raw_usr_data[0], raw_usr_data[1], raw_usr_data[3])
        else:
            raise FailedLoginException("Username or password is incorrect.")
    