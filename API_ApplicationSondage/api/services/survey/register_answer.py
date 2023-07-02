from dao import SurveyDAO
from ..constituent import CheckExists as ConstituentCheckExists
from ..food import CheckExists as FoodCheckExists
from .check_if_constituent_answer_exists import CheckIfConstituentAnswerExists

class RegisterAnswer:
    """Class for registering a survey answer for a constituent."""

    def __init__(self, constituent_id: int, survey_answer: list[int]):
        """
        Initialize a RegisterAnswer instance.

        Args:
            constituent_id (int): The ID of the constituent.
            survey_answer (list[int]): The list of food IDs representing the survey answer.
        """
        self.constituent_id = constituent_id
        self.survey_answer = survey_answer
        self.response = self.__register()
    
    def __register(self) -> dict:
        """
        Register a survey answer for a constituent.

        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        if len(self.survey_answer) != 10:
            return {"error": "Survey answer must be 10"}
        if CheckIfConstituentAnswerExists(self.constituent_id).get_response():
            return {"error": "Constituent already answered"}
        if not ConstituentCheckExists(self.constituent_id).get_response():
            return {"error": "Constituent does not exist"}
        for food_id in self.survey_answer:
            if not FoodCheckExists(food_id).get_response():
                return {"error": "Food does not exist"}
        try:
            with SurveyDAO() as survey_dao:
                survey_dao.register(self.constituent_id, self.survey_answer)
            return {"success": "Survey answer registered"}
        except Exception as e:
            print(e)
            return {"error": "Failed to register survey answer"}
    
    def get_response(self) -> dict:
        """
        Get the response of registering a survey answer.

        Returns:
            dict: A dictionary containing the response of registering a survey answer.
        """
        return self.response
