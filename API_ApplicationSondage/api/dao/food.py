from .database import Database

class FoodDAO:
    """
    Data Access Object (DAO) class for interacting with the Food data.

    Attributes:
        db (Database): an instance of Database class for interacting with the database.
    """

    def __init__(self) -> None:
        """
        Initialize a new instance of FoodDAO and connects to the database.
        """
        self.db = Database()
    
    def __enter__(self):
        """
        Context management method that gets a cursor from the database connection and returns itself.
        """
        self.cursor = self.db.get().cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context management method that closes the cursor and the database connection.
        """
        self.cursor.close()
        self.db.get().close()
    
    def get_groups(self) -> list[dict]:
        """
        Retrieves all the food groups from the database.

        Returns:
            A list of dictionaries where each dictionary represents a food group.
        """
        try:
            self.cursor.execute("SELECT * FROM food_groups")
            response = self.cursor.fetchall()
            # Return the response as a list of dictionaries
            response = [dict(zip([key[0] for key in self.cursor.description], row)) for row in response]
            return response
        except Exception as e:
            print(e)
            raise
    
    def check_exists(self, food_code: int) -> bool:
        """
        Checks if a food with the given food_code exists in the database.

        Args:
            food_code (int): The food_code of the food to check.

        Returns:
            True if the food exists, False otherwise.
        """
        try:
            self.cursor.execute("SELECT food_code FROM foods WHERE food_code = %s", (food_code,))
            return True if self.cursor.fetchone() else False
        except Exception as e:
            print(e)
            raise
    
    def get_subgroups_by_group(self, group_code: int) -> list[dict]:
        """
        Retrieves all the food subgroups for a given food group from the database.

        Args:
            group_code (int): The group_code of the food group.

        Returns:
            A list of dictionaries where each dictionary represents a food subgroup.
        """
        try:
            self.cursor.execute("SELECT * FROM food_subgroups WHERE group_code = %s", (group_code,))
            response = self.cursor.fetchall()
            # Return the response as a list of dictionaries
            response = [dict(zip([key[0] for key in self.cursor.description], row)) for row in response]
            return response
        except Exception as e:
            print(e)
            raise
    
    def get_sub_subgroups_by_subgroup(self, subgroup_code: int) -> list[dict]:
        """
        Retrieves all the food sub-subgroups for a given food subgroup from the database.

        Args:
            subgroup_code (int): The subgroup_code of the food subgroup.

        Returns:
            A list of dictionaries where each dictionary represents a food sub-subgroup.
        """
        try:
            self.cursor.execute("SELECT * FROM food_sub_subgroups WHERE subgroup_code = %s", (subgroup_code,))
            response = self.cursor.fetchall()
            # Return the response as a list of dictionaries
            response = [dict(zip([key[0] for key in self.cursor.description], row)) for row in response]
            return response
        except Exception as e:
            print(e)
            raise
    
    def get_foods_by_filter(self, group_code: int, subgroup_code: int = None, sub_subgroup_code: int = None) -> list[dict]:
        """
        Retrieves foods based on the provided filters. The filters can include group_code, subgroup_code, and sub_subgroup_code.

        Args:
            group_code (int): The group_code of the food group.
            subgroup_code (int, optional): The subgroup_code of the food subgroup.
            sub_subgroup_code (int, optional): The sub_subgroup_code of the food sub-subgroup.

        Returns:
            A list of dictionaries where each dictionary represents a food item.
        """
        try:
            if subgroup_code and sub_subgroup_code:
                self.cursor.execute("SELECT * FROM foods WHERE group_code = %s AND subgroup_code = %s AND sub_subgroup_code = %s", (group_code, subgroup_code, sub_subgroup_code))
            elif subgroup_code:
                self.cursor.execute("SELECT * FROM foods WHERE group_code = %s AND subgroup_code = %s", (group_code, subgroup_code))
            elif sub_subgroup_code:
                self.cursor.execute("SELECT * FROM foods WHERE group_code = %s AND sub_subgroup_code = %s", (group_code, sub_subgroup_code))
            else:
                self.cursor.execute("SELECT * FROM foods WHERE group_code = %s", (group_code,))
            response = self.cursor.fetchall()
            # Return the response as a list of dictionaries
            response = [dict(zip([key[0] for key in self.cursor.description], row)) for row in response]
            return response
        except Exception as e:
            print(e)
            raise
