"""
This module contains FastAPI route handlers for operations related to constituents.
These operations include registering a new constituent and deleting a constituent.

Available routes:
- POST /registerConstituent: Registers a new constituent.
- DELETE /deleteConstituent: Deletes a constituent.

Each of these route handlers may use an API key for authentication and validation.

Imports:
    - from fastapi import Query, HTTPException, status, APIRouter
    - from services.constituent import *
    - from models import Constituent

Classes:
    Constituent: Defines the data model for a constituent.

Functions:
    register_constituent(constituent: Constituent)
    delete_constituent(api_key: str, constituent_id: int)
"""

from fastapi import Query, HTTPException, status, APIRouter
from services.constituent import *
from models import Constituent

router = APIRouter()

@router.post("/registerConstituent", tags=["Constituent"])
def register_constituent(constituent: Constituent):
    response = Register(constituent.last_name, 
                        constituent.first_name, 
                        constituent.birth, 
                        constituent.address, 
                        constituent.postal_code, 
                        constituent.city, 
                        constituent.phone).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.delete("/deleteConstituent", tags=["Constituent"])
def delete_constituent(api_key: str,
                      constituent_id: int = Query(1, 
                                               title="constituent ID", 
                                               description="The ID of the constituent which you want to delete")):
    response = Delete(constituent_id, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response