"""
This module contains FastAPI route handlers for operations related to API keys.
These operations include creating, updating, deleting API keys, and retrieving all API keys for a specific super admin.

Available routes:
- GET /createAPIKey: Creates a new API key for a super admin.
- DELETE /deleteAPIKey: Deletes an API key.
- PUT /updateAPIKey: Updates the status of an API key (active/inactive).
- GET /getAll: Retrieves all API keys for a specific super admin.

Each of these route handlers uses an API key for authentication and validation.

Imports:
    - from fastapi import Query, HTTPException, status, APIRouter
    - from services.api_key import *
    - from models import APIKey, UpdateAPIKey

Classes:
    APIKey: Defines the data model for an API key.
    UpdateAPIKey: Defines the data model for updating an API key.

Functions:
    create_api_key(api_key: str, super_admin_id: int)
    delete_api_key(api_key: str, delete_api_key: APIKey)
    update_api_key(api_key: str, update_api_key: UpdateAPIKey)
    get_all(api_key: str, api_key_owner_id: int)
"""

from fastapi import Query, HTTPException, status, APIRouter
from services.api_key import *
from models import APIKey, UpdateAPIKey

router = APIRouter()

@router.get("/createAPIKey", tags=["API Key"])
def create_api_key(api_key: str, 
                     super_admin_id: int = Query(1, 
                                              title="Super Admin ID", 
                                              description="The ID of the super admin account which you want to generate an API key for")):
    response = Create(super_admin_id, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.delete("/deleteAPIKey", tags=["API Key"])
def delete_api_key(api_key: str, delete_api_key: str):
    response = Delete(delete_api_key, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.put("/updateAPIKey", tags=["API Key"])
def update_api_key(api_key: str, update_api_key: UpdateAPIKey):
    response = Update(update_api_key.api_key_owner_id, update_api_key.api_key, update_api_key.api_key_active, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.get("/getAll", tags=["API Key"])
def get_all(api_key: str):
    response = GetAll(api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response