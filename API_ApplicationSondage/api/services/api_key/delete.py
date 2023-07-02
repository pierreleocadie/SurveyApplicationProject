from dao import ApiKeyDAO
from utils.check_active import CheckActive
from .check import Check

class Delete:
    """Class for deleting an API key."""
    
    def __init__(self, api_key_to_delete: str, api_key: str = None) -> None:
        """
        Initialize a Delete instance.
        
        Args:
            api_key_to_delete (str): The API key to delete.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.api_key_to_delete = api_key_to_delete
        self.api_key = api_key
        self.response = self.__delete()
    
    def __delete(self) -> bool:
        """
        Delete an API key.
        
        Returns:
            bool: True if the API key was successfully deleted, False otherwise.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        if not Check(self.api_key_to_delete).get_response():
            return {"error": "API Key to delete does not exist"}
        try:
            with ApiKeyDAO() as api_key_dao:
                api_key_dao.delete(self.api_key_to_delete)
            return {"success": "API Key deleted"}
        except Exception as e:
            print(e)
            return {"error": "Failed to delete API Key"}
    
    def get_response(self) -> bool:
        """
        Get the response of the API key deletion.
        
        Returns:
            bool: True if the API key was successfully deleted, False otherwise.
        """
        return self.response
