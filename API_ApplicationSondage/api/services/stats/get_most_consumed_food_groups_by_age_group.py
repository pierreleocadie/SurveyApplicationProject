from dao import StatsDAO
from utils.check_active import CheckActive

class GetMostConsumedGroupsByAgeGroup:
    """Class for retrieving the most consumed food groups by age group."""
    
    def __init__(self, age_min: int, age_max: int, result_length: int, api_key: str = None) -> None:
        """
        Initialize a GetMostConsumedGroupsByAgeGroup instance.

        Args:
            age_min (int): The minimum age of the age group.
            age_max (int): The maximum age of the age group.
            result_length (int): The number of results to retrieve.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.age_min = age_min
        self.age_max = age_max
        self.result_length = result_length
        self.api_key = api_key
        self.response = self.__get_most_consumed_groups_by_age_group()
    
    def __get_most_consumed_groups_by_age_group(self) -> dict:
        """
        Retrieve the most consumed food groups by age group.

        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message and the data of most consumed groups.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        if self.age_min > self.age_max:
            return {"error": "age_min must be lower than age_max"}
        if self.result_length < 1:
            return {"error": "result_length must be greater than 0"}
        if self.age_min <= 19:
            return {"error": "age_min must be equal or greater than 20"}
        if self.age_max < self.age_min+2:
            return {"error": "age_max must be equal or greater than age_min+2"}
        try:
            with StatsDAO() as stats_dao:
                result = stats_dao.get_most_consumed_groups_by_age_group(self.age_min, self.age_max, self.result_length)
            return {"success": "Successfully got most consumed groups", "data": result}
        except Exception as e:
            print(e)
            return {"error": "Failed to get most consumed groups"}
    
    def get_response(self) -> dict:
        """
        Get the response of retrieving the most consumed food groups by age group.

        Returns:
            dict: A dictionary containing the response of retrieving the most consumed groups.
        """
        return self.response
