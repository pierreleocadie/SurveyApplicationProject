from dao import SurveyDAO

class CheckIfConstituentAnswerExists:
    """Class for checking if a constituent's answer exists in the survey."""

    def __init__(self, constituent_id: int):
        """
        Initialize a CheckIfConstituentAnswerExists instance.

        Args:
            constituent_id (int): The ID of the constituent.
        """
        self.constituent_id = constituent_id
        self.response = self.__check()
    
    def __check(self) -> bool:
        """
        Check if a constituent's answer exists in the survey.

        Returns:
            bool: True if the constituent's answer exists, False otherwise.
        """
        try:
            with SurveyDAO() as survey_dao:
                return survey_dao.check(self.constituent_id)
        except Exception as e:
            print(e)
            return False
    
    def get_response(self) -> bool:
        """
        Get the response of checking if a constituent's answer exists.

        Returns:
            bool: True if the constituent's answer exists, False otherwise.
        """
        return self.response
