"""
This module defines FastAPI route handlers for operations related to the survey system.
These operations include answering and deleting a survey.

Available routes:
- POST /answerSurvey: Handles a constituent's answer to a survey.
- DELETE /deleteAnswer: Deletes a constituent's answer to a survey.

Imports:
    - from fastapi import HTTPException, status, APIRouter
    - from services.survey import *

Functions:
    answer_survey(constituent_id: int, answer_survey: list[int])
    delete_survey(api_key: str, constituent_id: int)
"""

from fastapi import HTTPException, status, APIRouter
from services.survey import *

router = APIRouter()

@router.post("/answerSurvey", tags=["Survey"])
def answer_survey(constituent_id: int, answer_survey: list[int]):
    response = RegisterAnswer(constituent_id, answer_survey).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response

@router.delete("/deleteAnswer", tags=["Survey"])
def delete_survey(api_key: str, constituent_id: int):
    response = DeleteAnswer(constituent_id, api_key).get_response()
    if "error" in response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response["error"])
    else:
        return response