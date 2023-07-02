from dao import ApiKeyDAO
from utils.check_active import CheckActive
from ..admin import Get
from .check import Check

class Update:
    """Class for updating an API key."""
    
    def __init__(self, api_key_owner_id: int, api_key_to_update: str, api_key_active: bool, api_key: str = None) -> None:
        """
        Initialize an Update instance.
        
        Args:
            api_key_owner_id (int): The ID of the admin account that owns the API key.
            api_key_to_update (str): The API key to update.
            api_key_active (bool): The updated active status of the API key.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.api_key_owner_id = api_key_owner_id
        self.api_key_to_update = api_key_to_update
        self.api_key_active = api_key_active
        self.api_key = api_key
        self.response = self.__update()
    
    def __update(self) -> bool:
        """
        Update an API key.
        
        Returns:
            bool: True if the API key was successfully updated, False otherwise.
        """
        admin_account = Get(self.api_key_owner_id).get_response()
        if not admin_account:
            return {"error": "Admin account does not exist"}
        elif admin_account["role"] != "superadmin":
            return {"error": "You do not have permission to update API keys"}
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        if not Check(self.api_key_to_update).get_response():
            return {"error": "Invalid API Key to update"}
        try:
            with ApiKeyDAO() as api_key_dao:
                api_key_dao.update(self.api_key_owner_id, self.api_key_to_update, self.api_key_active)
            return {"success": "API key updated", "api_key": self.api_key_to_update, "api_key_owner_id": self.api_key_owner_id, "active": self.api_key_active}
        except Exception as e:
            print(e)
            return {"error": "Failed to update API key"}
    
    def get_response(self) -> bool:
        """
        Get the response of the API key update.
        
        Returns:
            bool: True if the API key was successfully updated, False otherwise.
        """
        return self.response
