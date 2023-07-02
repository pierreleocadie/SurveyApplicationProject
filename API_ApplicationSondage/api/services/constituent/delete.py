from dao import ConstituentDAO
from utils.check_active import CheckActive

class Delete:
    """Class for deleting a constituent."""

    def __init__(self, constituent_id: int, api_key: str = None) -> None:
        """
        Initialize a Delete instance.

        Args:
            constituent_id (int): The ID of the constituent to delete.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.constituent_id = constituent_id
        self.api_key = api_key
        self.response = self.__delete()

    def __delete(self) -> dict:
        """
        Delete a constituent.

        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        if __name__ != "__main__":
            if not CheckActive(self.api_key).get_response():
                return {"error": "Invalid API Key"}
        try:
            with ConstituentDAO() as constituent_dao:
                constituent_dao.delete(self.constituent_id)
            return {"success": "Constituent deleted"}
        except Exception as e:
            print(e)
            return {"error": "Failed to delete constituent"}

    def get_response(self) -> dict:
        """
        Get the response of the constituent deletion.

        Returns:
            dict: A dictionary containing the response of the constituent deletion.
        """
        return self.response
