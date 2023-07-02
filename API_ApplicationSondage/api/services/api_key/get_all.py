from dao import ApiKeyDAO
from ..admin import Get
from utils.check_active import CheckActive

class GetAll:
    """Class for retrieving all API keys."""
    
    def __init__(self, api_key: str = None) -> None:
        """
        Initialize a GetAll instance.
        
        Args:
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.api_key = api_key
        self.response = self.__get()
    
    def __get(self) -> bool | dict:
        """
        Retrieve all API keys.
        
        Returns:
            bool | dict: If successful, a dictionary containing the response of the operation.
                The dictionary will have a "success" key with a message and a "data" key with the API keys information.
                If unsuccessful, the dictionary will have an "error" key with a message.
                If there are no API keys found, the dictionary will have an "error" key with a "No API Keys found" message.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        
        try:
            with ApiKeyDAO() as api_key_dao:
                response = api_key_dao.get_all()
            return {"success": "API Keys info retrieved", "data": response}
        except Exception as e:
            if str(e) == "No API Keys found":
                return {"error": "No API Keys found"}
            print(e)
            return {"error": "An error occurred while getting API Keys info"}
    
    def get_response(self) -> bool | dict:
        """
        Get the response of retrieving all API keys.
        
        Returns:
            bool | dict: If successful, a dictionary containing the response of retrieving all API keys.
        """
        return self.response
