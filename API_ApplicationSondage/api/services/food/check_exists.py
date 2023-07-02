from dao import FoodDAO

class CheckExists:
    """Class for checking the existence of a food item."""

    def __init__(self, food_code: int):
        """
        Initialize a CheckExists instance.

        Args:
            food_code (int): The code of the food item to check.
        """
        self.food_code = food_code
        self.response = self.__check()

    def __check(self) -> bool:
        """
        Check the existence of a food item.

        Returns:
            bool: True if the food item exists, False otherwise.
        """
        try:
            with FoodDAO() as food_dao:
                return food_dao.check_exists(self.food_code)
        except Exception as e:
            print(e)
            return False

    def get_response(self) -> bool:
        """
        Get the response of the food item existence check.

        Returns:
            bool: True if the food item exists, False otherwise.
        """
        return self.response