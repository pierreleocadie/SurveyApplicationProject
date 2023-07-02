from dao import ConstituentDAO

class CheckExists:
    """Class for checking the existence of a constituent."""
    
    def __init__(self, constituent_id: int):
        """
        Initialize a CheckExists instance.
        
        Args:
            constituent_id (int): The ID of the constituent to check.
        """
        self.constituent_id = constituent_id
        self.response = self.__check()
    
    def __check(self) -> bool:
        """
        Check the existence of a constituent.
        
        Returns:
            bool: True if the constituent exists, False otherwise.
        """
        try:
            with ConstituentDAO() as constituent_dao:
                return constituent_dao.get(self.constituent_id)
        except Exception as e:
            print(e)
            return False
    
    def get_response(self) -> bool:
        """
        Get the response of the constituent existence check.
        
        Returns:
            bool: True if the constituent exists, False otherwise.
        """
        return self.response
