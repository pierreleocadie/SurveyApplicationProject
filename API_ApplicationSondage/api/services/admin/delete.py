from utils.check_active import CheckActive
from dao import AdminDAO
from .get import Get

class Delete:
    """Class for deleting an admin account."""
    
    def __init__(self, username: str, api_key: str = None) -> None:
        """
        Initialize a Delete instance.
        
        Args:
            username (str): The username of the admin account to delete.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.username = username
        self.api_key = api_key
        self.response = self.__delete()
    
    def __delete(self) -> dict:
        """
        Delete an admin account.
        
        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        
        if not Get(username=self.username).get_response():
            return {"error": "Admin Account Does Not Exist"}
        
        try:
            with AdminDAO() as admin_dao:
                admin_dao.delete(username=self.username)
            return {"success": "Admin account deleted"}
        except Exception as e:
            print(e)
            return {"error": "Failed to delete admin account"}
    
    def get_response(self) -> dict:
        """
        Get the response of the admin account deletion.
        
        Returns:
            dict: A dictionary containing the response of the admin account deletion.
        """
        return self.response
