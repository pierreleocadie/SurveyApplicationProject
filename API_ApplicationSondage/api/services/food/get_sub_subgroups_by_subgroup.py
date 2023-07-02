from dao import FoodDAO

class GetSubSubgroupsBySubgroup:
    """Class for retrieving sub-subgroups of foods based on a subgroup."""

    def __init__(self, subgroup_code: int):
        """
        Initialize a GetSubSubgroupsBySubgroup instance.

        Args:
            subgroup_code (int): The code of the subgroup to retrieve sub-subgroups for.
        """
        self.subgroup_code = subgroup_code
        self.response = self.__get()
    
    def __get(self) -> dict:
        """
        Retrieve sub-subgroups of foods based on a subgroup.

        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message and the data of sub-subgroups.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        try:
            with FoodDAO() as food_dao:
                response = food_dao.get_sub_subgroups_by_subgroup(self.subgroup_code)
            return {"success": "Sub-subgroups of foods fetched", "data": response}
        except Exception as e:
            print(e)
            return {"error": "Failed to fetch sub-subgroups of foods"}
    
    def get_response(self) -> dict:
        """
        Get the response of retrieving sub-subgroups of foods based on a subgroup.

        Returns:
            dict: A dictionary containing the response of retrieving sub-subgroups of foods.
        """
        return self.response
