"""
This module contains FastAPI route handlers for operations related to admin accounts.
These operations include creating, updating, deleting admin accounts, and also admin login functionality.

Available routes:
- POST /createAdminAccount: Creates a new admin account.
- PUT /updateAdminAccount: Updates an existing admin account.
- DELETE /deleteAdminAccount: Deletes an existing admin account.
- POST /login: Authenticates an admin and logs them in.

Each of these route handlers uses an API key for authentication and validation.

Imports:
    - from fastapi import Query, HTTPException, status, APIRouter
    - from services.admin import *
    - from models import Admin, AdminLogin

Classes:
    Admin: Defines the data model for an admin account.
    AdminLogin: Defines the data model for admin login.

Functions:
    create_admin_account(api_key: str, admin_account: Admin)
    update_admin_account(api_key: str, admin_account: Admin)
    delete_admin_account(api_key: str, admin_username: str)
    login(admin_account: AdminLogin)
"""

from fastapi import Query, HTTPException, status, APIRouter
from services.admin import *
from models import Admin, AdminLogin

router = APIRouter()

@router.post("/createAdminAccount", tags=["Admin Account"])
def create_admin_account(api_key: str, admin_account: Admin):
    response = Create(admin_account.username, admin_account.password, admin_account.role, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.put("/updateAdminAccount", tags=["Admin Account"])
def update_admin_account(api_key: str, admin_account: Admin):
    response =  Update(admin_account.username, admin_account.password, admin_account.role, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.delete("/deleteAdminAccount", tags=["Admin Account"])
def delete_admin_account(api_key: str, 
                         admin_username: str = Query("test", 
                                                   title="Username", 
                                                   description="The username of the admin account which you want to delete", 
                                                   min_length=4, 
                                                   max_length=10)):
    response  = Delete(admin_username, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.post("/login", tags=["Admin Account"])
def login(admin_account: AdminLogin):
    response = Login(admin_account.username, admin_account.password).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response