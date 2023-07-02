from dao import SurveyDAO
from utils.check_active import CheckActive
from .check_if_constituent_answer_exists import CheckIfConstituentAnswerExists

class DeleteAnswer:
    """Class for deleting a survey answer of a constituent."""

    def __init__(self, constituent_id: int, api_key: str):
        """
        Initialize a DeleteAnswer instance.

        Args:
            constituent_id (int): The ID of the constituent.
            api_key (str): The API key for authentication.
        """
        self.api_key = api_key
        self.constituent_id = constituent_id
        self.response = self.__delete()
    
    def __delete(self) -> dict:
        """
        Delete a survey answer of a constituent.

        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        if not CheckIfConstituentAnswerExists(constituent_id=self.constituent_id).get_response():
            return {"error": "Constituent does not have any answers"}
        try:
            with SurveyDAO() as survey_dao:
                survey_dao.delete(self.constituent_id)
            return {"success": "Survey answer deleted"}
        except Exception as e:
            print(e)
            return {"error": "Failed to delete survey answer"}
    
    def get_response(self) -> dict:
        """
        Get the response of deleting a survey answer.

        Returns:
            dict: A dictionary containing the response of deleting a survey answer.
        """
        return self.response
