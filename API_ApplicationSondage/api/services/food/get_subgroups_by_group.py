from dao import FoodDAO

class GetSubgroupsByGroup:
    """Class for retrieving subgroups of foods based on a group."""

    def __init__(self, group_code: int):
        """
        Initialize a GetSubgroupsByGroup instance.

        Args:
            group_code (int): The code of the group to retrieve subgroups for.
        """
        self.group_code = group_code
        self.response = self.__get()
    
    def __get(self) -> dict:
        """
        Retrieve subgroups of foods based on a group.

        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message and the data of subgroups.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        try:
            with FoodDAO() as food_dao:
                response = food_dao.get_subgroups_by_group(self.group_code)
            return {"success": "Subgroups of foods fetched", "data": response}
        except Exception as e:
            print(e)
            return {"error": "Failed to fetch subgroups of foods"}
    
    def get_response(self) -> dict:
        """
        Get the response of retrieving subgroups of foods based on a group.

        Returns:
            dict: A dictionary containing the response of retrieving subgroups of foods.
        """
        return self.response
