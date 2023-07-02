from dao import FoodDAO

class GetGroups:
    """Class for retrieving food groups."""

    def __init__(self):
        """
        Initialize a GetGroups instance.
        """
        self.response = self.__get()
    
    def __get(self) -> dict:
        """
        Retrieve food groups.

        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message and the data of food groups.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        try:
            with FoodDAO() as food_dao:
                response = food_dao.get_groups()
            return {"success": "Food groups fetched", "data": response}
        except Exception as e:
            print(e)
            return {"error": "Failed to fetch food groups"}
    
    def get_response(self) -> dict:
        """
        Get the response of retrieving food groups.

        Returns:
            dict: A dictionary containing the response of retrieving food groups.
        """
        return self.response
