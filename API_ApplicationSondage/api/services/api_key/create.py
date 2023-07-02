import uuid
from ..admin import Get
from dao import ApiKeyDAO
from utils.check_active import CheckActive


class Create:
    """Class for creating an API key."""
    
    def __init__(self, admin_id: int = None, api_key: str = None) -> None:
        """
        Initialize a Create instance.
        
        Args:
            admin_id (int, optional): The ID of the admin account. Defaults to None.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.admin_id = admin_id
        self.api_key = api_key
        self.response = self.__create()
    
    def __create(self) -> dict:
        """
        Create an API key.
        
        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message,
                the generated API key, the API key owner's ID, and the active status.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
            admin_account = Get(self.admin_id).get_response()
            if not admin_account:
                return {"error": "Admin account does not exist"}
            elif admin_account["role"] != "superadmin":
                return {"error": "You do not have permission to generate API keys"}
        
        try:
            random_api_key_gen: str = uuid.uuid4().hex
            with ApiKeyDAO() as api_key_dao:
                api_key_dao.create(self.admin_id, random_api_key_gen)
            return {
                "success": "API key generated",
                "api_key": random_api_key_gen,
                "api_key_owner_id": self.admin_id,
                "active": True
            }
        except Exception as e:
            print(e)
            return {"error": "Failed to generate API key"}
    
    def get_response(self) -> dict:
        """
        Get the response of the API key creation.
        
        Returns:
            dict: A dictionary containing the response of the API key creation.
        """
        return self.response
