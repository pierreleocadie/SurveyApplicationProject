from .database import Database

class StatsDAO:
    """
    Data Access Object (DAO) class for interacting with the statistics data.

    Attributes:
        db (Database): an instance of Database class for interacting with the database.
    """
    
    def __init__(self) -> None:
        """
        Initialize a new instance of StatsDAO and connects to the database.
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
    
    def get_most_consumed_foods_by_age_group(self, age_min: int, age_max: int, result_length: int) -> dict:
        """
        Retrieves the most consumed foods by a specific age group from the database.

        Args:
            age_min (int): The minimum age for the age group.
            age_max (int): The maximum age for the age group.
            result_length (int): The maximum number of results to return.

        Returns:
            A dictionary where each key is a food and each value is the number of times the food was consumed.
        """
        try:
            # Load all foods from database
            self.cursor.execute("SELECT * FROM foods")
            foods: list = self.cursor.fetchall()
            
            # Load all constituents from database
            self.cursor.execute("SELECT constituent_id, TIMESTAMPDIFF(YEAR, birth, CURDATE()) AS age FROM constituents WHERE TIMESTAMPDIFF(YEAR, birth, CURDATE()) >= %s AND TIMESTAMPDIFF(YEAR, birth, CURDATE()) <= %s", (age_min, age_max,))
            constituents: list = self.cursor.fetchall()
            
            # Load survey answers that correspond to the constituents
            self.cursor.execute("SELECT * FROM survey WHERE constituent_id IN (" + ",".join([str(constituent[0]) for constituent in constituents]) + ")")
            survey: list = self.cursor.fetchall()
            
            foods_count: dict = {}
            for answer in survey:
                for food in answer[1:]:
                    if food in foods_count.keys():
                        foods_count[food] += 1
                    else:
                        foods_count[food] = 1
            
            # Replace food id by food name
            for food in foods:
                for food_code in foods_count.keys():
                    if food_code == food[0]:
                        foods_count[food[1]] = foods_count.pop(food_code)
                        break
            
            # Sort the result by the number of times an food appears in the survey answers
            result = {k: v for k, v in sorted(foods_count.items(), key=lambda item: item[1], reverse=True)}
            
            # Keep only the first n elements
            result = dict(list(result.items())[:result_length])
            return result
        except Exception as e:
            print(e)
            raise
    
    def get_most_consumed_groups_by_age_group(self, age_min: int, age_max: int, result_length: int) -> dict:
        """
        Retrieves the most consumed food groups by a specific age group from the database.

        Args:
            age_min (int): The minimum age for the age group.
            age_max (int): The maximum age for the age group.
            result_length (int): The maximum number of results to return.

        Returns:
            A dictionary where each key is a food group and each value is the number of times foods from this group were consumed.
        """
        try:
            # Load all foods from database
            self.cursor.execute("SELECT foods.food_code, foods.food_name_fr, foods.group_code, food_groups.group_name_fr FROM foods INNER JOIN food_groups ON foods.group_code = food_groups.group_code")
            foods: list = self.cursor.fetchall()
            
            # Load all constituents from database
            self.cursor.execute("SELECT constituent_id, TIMESTAMPDIFF(YEAR, birth, CURDATE()) AS age FROM constituents WHERE TIMESTAMPDIFF(YEAR, birth, CURDATE()) >= %s AND TIMESTAMPDIFF(YEAR, birth, CURDATE()) <= %s", (age_min, age_max,))
            constituents: list = self.cursor.fetchall()
            
            # Load survey answers that correspond to the constituents
            self.cursor.execute("SELECT * FROM survey WHERE constituent_id IN (" + ",".join([str(constituent[0]) for constituent in constituents]) + ")")
            survey: list = self.cursor.fetchall()
            
            # Count the number of times an food groupe appears in the survey answers
            groupsCount: dict = {}
            for answer in survey:
                for food in foods:
                    if food[0] in answer[1:]:
                        if food[3] in groupsCount.keys():
                            groupsCount[food[3]] += 1
                        else:
                            groupsCount[food[3]] = 1
            
            # Sort the result by the number of times an food groupe appears in the survey answers
            result = {k: v for k, v in sorted(groupsCount.items(), key=lambda item: item[1], reverse=True)}
            
            # Keep only the first n results
            result = {k: result[k] for k in list(result.keys())[:result_length]}
            return result
        except Exception as e:
            print(e)
            raise
    
    def get_most_consumed_sub_subgroups_by_age_group(self, age_min: int, age_max: int, result_length: int) -> dict:
        """
        Retrieves the most consumed food sub-subgroups by a specific age group from the database.

        Args:
            age_min (int): The minimum age for the age group.
            age_max (int): The maximum age for the age group.
            result_length (int): The maximum number of results to return.

        Returns:
            A dictionary where each key is a food sub-subgroup and each value is the number of times foods from this sub-subgroup were consumed.
        """
        try:
            # Load all foods from database
            self.cursor.execute("SELECT foods.food_code, foods.food_name_fr, foods.sub_subgroup_code, food_sub_subgroups.sub_subgroup_name_fr FROM foods INNER JOIN food_sub_subgroups ON foods.sub_subgroup_code = food_sub_subgroups.sub_subgroup_code")
            foods: list = self.cursor.fetchall()
            
            # Load all constituents from database
            self.cursor.execute("SELECT constituent_id, TIMESTAMPDIFF(YEAR, birth, CURDATE()) AS age FROM constituents WHERE TIMESTAMPDIFF(YEAR, birth, CURDATE()) >= %s AND TIMESTAMPDIFF(YEAR, birth, CURDATE()) <= %s", (age_min, age_max,))
            constituents: list = self.cursor.fetchall()
            
            # Load survey answers that correspond to the constituents
            self.cursor.execute("SELECT * FROM survey WHERE constituent_id IN (" + ",".join([str(constituent[0]) for constituent in constituents]) + ")")
            survey: list = self.cursor.fetchall()
            
            # Count the number of times an food sous groupe appears in the survey answers
            sub_subgroups_count: dict = {}
            for answer in survey:
                for food in foods:
                    if food[0] in answer[1:]:
                        if food[3] in sub_subgroups_count.keys():
                            sub_subgroups_count[food[3]] += 1
                        else:
                            sub_subgroups_count[food[3]] = 1
            
            # Sort the result by the number of times an food sous groupe appears in the survey answers
            result = {k: v for k, v in sorted(sub_subgroups_count.items(), key=lambda item: item[1], reverse=True)}
            
            # Keep only the first n results
            result = {k: result[k] for k in list(result.keys())[:result_length]}
            return result
        except Exception as e:
            print(e)
            raise
    
    def get_most_consumed_subgroups_by_age_group(self, age_min: int, age_max: int, result_length: int) -> dict:
        """
        Retrieves the most consumed food subgroups by a specific age group from the database.

        Args:
            age_min (int): The minimum age for the age group.
            age_max (int): The maximum age for the age group.
            result_length (int): The maximum number of results to return.

        Returns:
            A dictionary where each key is a food subgroup and each value is the number of times foods from this subgroup were consumed.
        """
        try:
            # Load all foods from database
            self.cursor.execute("SELECT foods.food_code, foods.food_name_fr, foods.subgroup_code, food_subgroups.subgroup_name_fr FROM foods INNER JOIN food_subgroups ON foods.subgroup_code = food_subgroups.subgroup_code")
            foods: list = self.cursor.fetchall()
            
            # Load all constituents from database
            self.cursor.execute("SELECT constituent_id, TIMESTAMPDIFF(YEAR, birth, CURDATE()) AS age FROM constituents WHERE TIMESTAMPDIFF(YEAR, birth, CURDATE()) >= %s AND TIMESTAMPDIFF(YEAR, birth, CURDATE()) <= %s", (age_min, age_max,))
            constituents: list = self.cursor.fetchall()
            
            # Load survey answers that correspond to the constituents
            self.cursor.execute("SELECT * FROM survey WHERE constituent_id IN (" + ",".join([str(constituent[0]) for constituent in constituents]) + ")")
            survey: list = self.cursor.fetchall()
            
            # Count the number of times an food sous groupe appears in the survey answers
            subgroups_count: dict = {}
            for answer in survey:
                for food in foods:
                    if food[0] in answer[1:]:
                        if food[3] in subgroups_count.keys():
                            subgroups_count[food[3]] += 1
                        else:
                            subgroups_count[food[3]] = 1
            
            # Sort the result by the number of times an food sous groupe appears in the survey answers
            result = {k: v for k, v in sorted(subgroups_count.items(), key=lambda item: item[1], reverse=True)}
            
            # Keep only the first n results
            result = {k: result[k] for k in list(result.keys())[:result_length]}
            return result
        except Exception as e:
            print(e)
            raise
        