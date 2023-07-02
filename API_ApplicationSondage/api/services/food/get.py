from dao import FoodDAO

class Get:
    """Class for retrieving foods based on filter criteria."""

    def __init__(self, group_code: int, subgroup_code: int = None, sub_subgroup_code: int = None):
        """
        Initialize a Get instance.

        Args:
            group_code (int): The code of the group to filter foods by.
            subgroup_code (int, optional): The code of the subgroup to filter foods by. Defaults to None.
            sub_subgroup_code (int, optional): The code of the sub-subgroup to filter foods by. Defaults to None.
        """
        self.group_code = group_code
        self.subgroup_code = subgroup_code
        self.sub_subgroup_code = sub_subgroup_code
        self.response = self.__get()
    
    def __get(self) -> dict:
        """
        Retrieve foods based on filter criteria.

        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message and the data of foods.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        try:
            with FoodDAO() as food_dao:
                response = food_dao.get_foods_by_filter(self.group_code, self.subgroup_code, self.sub_subgroup_code)
            return {"success": "Foods fetched", "data": response}
        except Exception as e:
            print(e)
            return {"error": "Failed to fetch foods"}
    
    def get_response(self) -> dict:
        """
        Get the response of retrieving foods based on filter criteria.

        Returns:
            dict: A dictionary containing the response of retrieving foods.
        """
        return self.response
