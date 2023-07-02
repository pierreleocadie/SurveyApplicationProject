"""
This module defines FastAPI route handlers for operations related to consumption statistics.
These operations include fetching most consumed foods, groups, subgroups, and sub-subgroups by age group.

Available routes:
- GET /getMostConsumedFoodsByAgeGroup: Retrieves the most consumed foods for a specified age group.
- GET /getMostConsumedGroupsByAgeGroup: Retrieves the most consumed food groups for a specified age group.
- GET /getMostConsumedSubgroupsByAgeGroup: Retrieves the most consumed food subgroups for a specified age group.
- GET /getMostConsumedSubSubgroupsByAgeGroup: Retrieves the most consumed food sub-subgroups for a specified age group.

Imports:
    - from fastapi import HTTPException, status, APIRouter
    - from services.stats import *

Functions:
    get_most_consumed_foods_by_age_group(age_min: int, age_max: int, result_length: int, api_key: str)
    get_most_consumed_groups_by_age_group(age_min: int, age_max: int, result_length: int, api_key: str)
    get_most_consumed_subgroups_by_age_group(age_min: int, age_max: int, result_length: int, api_key: str)
    get_most_consumed_sub_subgroups_by_age_group(age_min: int, age_max: int, result_length: int, api_key: str)
"""

from fastapi import HTTPException, status, APIRouter
from services .stats import *

router = APIRouter()

@router.get("/getMostConsumedFoodsByAgeGroup", tags=["Stats"])
def get_most_consumed_foods_by_age_group(age_min: int, age_max: int, result_length: int, api_key: str):
    response = GetMostConsumedFoodsByAgeGroup(age_min, age_max, result_length, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.get("/getMostConsumedGroupsByAgeGroup", tags=["Stats"])
def get_most_consumed_groups_by_age_group(age_min: int, age_max: int, result_length: int, api_key: str):
    response = GetMostConsumedGroupsByAgeGroup(age_min, age_max, result_length, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.get("/getMostConsumedSubgroupsByAgeGroup", tags=["Stats"])
def get_most_consumed_subgroups_by_age_group(age_min: int, age_max: int, result_length: int, api_key: str):
    response = GetMostConsumedSubgroupsByAgeGroup(age_min, age_max, result_length, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.get("/getMostConsumedSubSubgroupsByAgeGroup", tags=["Stats"])
def get_most_consumed_sub_subgroups_by_age_group(age_min: int, age_max: int, result_length: int, api_key: str):
    response = GetMostConsumedSubSubgroupsByAgeGroup(age_min, age_max, result_length, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response