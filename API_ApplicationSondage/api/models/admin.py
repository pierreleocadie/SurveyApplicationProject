from pydantic import BaseModel, Field
from enum import Enum

class AdminRole(str, Enum):
    """
    AdminRole Enum class.

    Defines the possible roles an admin can have: superadmin and admin.
    """
    superadmin = "superadmin"
    admin = "admin"

class Username(BaseModel):
    """
    Username Model class.

    Defines the structure of the 'Username' attribute with Pydantic validation.

    Attributes:
    - username (str): The username of the admin account which should be unique. The field has a minimum length of 4 and a maximum length of 10.
    """
    username: str = Field("test", 
                          title="Username", 
                          description="Username of the admin account must be unique", 
                          min_length=4, 
                          max_length=10)

class Password(BaseModel):
    """
    Password Model class.

    Defines the structure of the 'Password' attribute with Pydantic validation.

    Attributes:
    - password (str): The password of the admin account. The field has a minimum length of 6.
    """
    password: str = Field("testtest",
                          title="Password",
                          description="Password of the admin account",
                          min_length=6)

class Admin(Username, Password):
    """
    Admin Model class.

    Inherits from the 'Username' and 'Password' models and adds an additional attribute for the admin's role.

    Attributes:
    - role (AdminRole): The role of the admin account which can be either 'admin' or 'superadmin'.
    """
    role: AdminRole = Field("admin", 
                      title="Role", 
                      description="Role of the admin account", 
                      regex="^(admin|superadmin)$")

class AdminLogin(Username, Password):
    """
    AdminLogin Model class.

    Inherits from the 'Username' and 'Password' models and used for validating login details of an admin.
    """
    ...