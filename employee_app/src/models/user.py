from enums.role_enum import Role
from exceptions.invalid_role_exception import InvalidRoleException

class User:
    id : int
    username : str
    role : Role
    
    def __init__(self, id : int, username : str, role : Role):
        self.id = id
        self.username = username
        self.role = role
    
    @classmethod
    def from_str_role(cls, id : int, username : str, role : str):
        if role == 'EMPLOYEE':
            role = Role.EMPLOYEE
        elif role == 'MANAGER':
            role = Role.MANAGER
        else:
            raise InvalidRoleException("Role must be 'Employee' or 'Manager'.")
        
        return cls(id, username, role)