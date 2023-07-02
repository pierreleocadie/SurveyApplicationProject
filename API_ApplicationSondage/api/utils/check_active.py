from dao import ApiKeyDAO

class CheckActive:
    """
    Class for checking the active status of an API key.

    Args:
    - api_key (str): The API key to check.

    Attributes:
    - api_key (str): The API key to check.
    - response (bool): The response indicating the active status of the API key.

    Methods:
    - _check(): Private method to check the active status of the API key.
    - get_response(): Method to retrieve the response indicating the active status.

    Note: This class interacts with the `ApiKeyDAO` data access object to perform the check.
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.response = self._check()
    
    def _check(self) -> bool:
        """
        Private method to check the active status of the API key.

        Returns:
        - bool: True if the API key is active, False otherwise.
        """
        try:
            with ApiKeyDAO() as api_key_dao:
                return api_key_dao.check_active(self.api_key)
        except Exception as e:
            print(e)
            return False
    
    def get_response(self) -> bool:
        """
        Method to retrieve the response indicating the active status of the API key.

        Returns:
        - bool: True if the API key is active, False otherwise.
        """
        return self.response
