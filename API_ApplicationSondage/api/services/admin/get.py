from dao import AdminDAO

class Get:
    """Class for retrieving admin account information."""
    
    def __init__(self, admin_id: int = None, username: str = None) -> None:
        """
        Initialize a Get instance.
        
        Args:
            admin_id (int, optional): The ID of the admin account to retrieve. Defaults to None.
            username (str, optional): The username of the admin account to retrieve. Defaults to None.
        """
        self.admin_id = admin_id
        self.username = username
        self.response = self.__get()
    
    def __get(self) -> dict:
        """
        Retrieve admin account information.
        
        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will contain the admin account information.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        try:
            with AdminDAO() as admin_dao:
                if self.admin_id:
                    response = admin_dao.get(admin_id=self.admin_id)
                elif self.username:
                    response = admin_dao.get(username=self.username)
                else:
                    return {"error": "Invalid parameters"}
            return response
        except Exception as e:
            print(e)
            return {"error": "Failed to get admin account"}
    
    def get_response(self) -> dict:
        """
        Get the response of the admin account retrieval.
        
        Returns:
            dict: A dictionary containing the response of the admin account retrieval.
        """
        return self.response
