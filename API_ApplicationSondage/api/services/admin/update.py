from utils.check_active import CheckActive
from dao import AdminDAO
from .get import Get


class Update:
    """Class for updating an admin account."""
    
    def __init__(self, username: str, password: str, role: str, api_key: str = None) -> None:
        """
        Initialize an Update instance.
        
        Args:
            username (str): The username of the admin account to update.
            password (str): The new password for the admin account.
            role (str): The new role for the admin account.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.username = username
        self.password = password
        self.role = role
        self.api_key = api_key
        self.response = self.__update()
    
    def __update(self) -> dict:
        """
        Update an admin account.
        
        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        
        try:
            if not Get(username=self.username).get_response():
                return {"error": "Admin Account Does Not Exist"}
            
            with AdminDAO() as admin_dao:
                admin_dao.update(username=self.username, password=self.password, role=self.role)
            return {"success": "Admin account updated"}
        except Exception as e:
            print(e)
            return {"error": "Failed to update admin account"}
    
    def get_response(self) -> dict:
        """
        Get the response of the admin account update.
        
        Returns:
            dict: A dictionary containing the response of the admin account update.
        """
        return self.response
