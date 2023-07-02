from dao import ApiKeyDAO

class Check:
    """Class for checking the validity of an API key."""
    
    def __init__(self, api_key: str) -> None:
        """
        Initialize a Check instance.
        
        Args:
            api_key (str): The API key to check.
        """
        self.api_key = api_key
        self.response = self.__check()
    
    def __check(self) -> bool:
        """
        Check the validity of the API key.
        
        Returns:
            bool: True if the API key is valid, False otherwise.
        """
        try:
            with ApiKeyDAO() as api_key_dao:
                return api_key_dao.check(self.api_key)
        except Exception as e:
            print(e)
            return False
    
    def get_response(self) -> bool:
        """
        Get the response of the API key check.
        
        Returns:
            bool: True if the API key is valid, False otherwise.
        """
        return self.response
