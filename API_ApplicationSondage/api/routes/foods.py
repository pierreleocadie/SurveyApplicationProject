"""
This module contains FastAPI route handlers for operations related to food items. 
These operations include fetching food items, groups, subgroups, and sub-subgroups.

Available routes:
- GET /getFoods: Retrieves food items based on provided group, subgroup and sub-subgroup codes.
- GET /getGroups: Retrieves all food groups.
- GET /getSubgroups: Retrieves all food subgroups for a specific food group.
- GET /getSubSubgroups: Retrieves all food sub-subgroups for a specific food subgroup.

Imports:
    - from fastapi import HTTPException, status, APIRouter
    - from services.food import *
    - from typing import Optional

Functions:
    get_foods(group_code: int, subgroup_code: Optional[int] = None, sub_subgroup_code: Optional[int] = None)
    get_food_groups()
    get_food_subgroups_by_group(group_code: int)
    get_food_sub_subgroups_by_subgroup(subgroup_code: int)
"""

from fastapi import HTTPException, status, APIRouter
from services.food import *
from typing import Optional

router = APIRouter()

@router.get("/getFoods", tags=["Foods"])
def get_foods(group_code: int, subgroup_code: Optional[int] = None, sub_subgroup_code: Optional[int] = None):
    response = Get(group_code, subgroup_code, sub_subgroup_code).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.get("/getGroups", tags=["Foods"])
def get_food_groups():
    response = GetGroups().get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.get("/getSubgroups", tags=["Foods"])
def get_food_subgroups_by_group(group_code: int):
    response = GetSubgroupsByGroup(group_code).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.get("/getSubSubgroups", tags=["Foods"])
def get_food_sub_subgroups_by_subgroup(subgroup_code: int):
    response = GetSubSubgroupsBySubgroup(subgroup_code).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response