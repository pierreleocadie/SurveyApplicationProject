import bcrypt
from .get import Get

class Login:
    """Class for user login authentication."""
    
    def __init__(self, username: str, password: str) -> None:
        """
        Initialize a Login instance.
        
        Args:
            username (str): The username for login authentication.
            password (str): The password for login authentication.
        """
        self.username = username
        self.password = password
        self.response = self.__login()
    
    def __login(self) -> dict:
        """
        Authenticate the user login.
        
        Returns:
            dict: A dictionary containing the response of the authentication.
                If successful, the dictionary will contain the user information.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        try:
            response = Get(username=self.username).get_response()
            
            if not response:
                return {"error": "Invalid username or password"}
            
            if bcrypt.checkpw(self.password.encode("utf-8"), response["password"].encode("utf-8")):
                return response
            return {"error": "Invalid username or password"}
        except Exception as e:
            print(e)
            return {"error": "Failed to login"}
    
    def get_response(self) -> dict:
        """
        Get the response of the login authentication.
        
        Returns:
            dict: A dictionary containing the response of the login authentication.
        """
        return self.response
