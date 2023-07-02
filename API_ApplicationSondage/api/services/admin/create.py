from utils.check_active import CheckActive
from dao import AdminDAO

class Create:
    """Class for creating an admin account."""
    
    def __init__(self, username: str, password: str, role: str, api_key: str = None) -> None:
        """
        Initialize a Create instance.
        
        Args:
            username (str): The username of the admin account.
            password (str): The password of the admin account.
            role (str): The role of the admin account.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.username = username
        self.password = password
        self.role = role
        self.api_key = api_key
        self.response = self.__create()
    
    def __create(self) -> dict:
        """
        Create an admin account.
        
        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        
        try:
            with AdminDAO() as admin_dao:
                if admin_dao.get(username=self.username):
                    return {"error": "Admin Account Already Exists"}
                admin_dao.create(username=self.username, password=self.password, role=self.role)
            return {"success": "Admin account created"}
        except Exception as e:
            print(e)
            return {"error": "Failed to create admin account"}
    
    def get_response(self) -> dict:
        """
        Get the response of the admin account creation.
        
        Returns:
            dict: A dictionary containing the response of the admin account creation.
        """
        return self.response