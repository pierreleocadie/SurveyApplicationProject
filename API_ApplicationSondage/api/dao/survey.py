from .database import Database

class SurveyDAO:
    """
    Data Access Object (DAO) class for interacting with survey data.

    Attributes:
        db (Database): an instance of Database class for interacting with the database.
    """
    
    def __init__(self) -> None:
        """
        Initialize a new instance of SurveyDAO and connects to the database.
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
    
    def register(self, constituent_id: int, survey_answer: list[int]) -> bool:
        """
        Register a new survey response into the database.

        Args:
            constituent_id (int): The identifier of the constituent who answered the survey.
            survey_answer (list[int]): The list of food codes chosen by the constituent.

        Returns:
            bool: True if the operation was successful, raises an exception otherwise.
        """
        try:
            self.cursor.execute("INSERT INTO survey(constituent_id, food_code_1, food_code_2, food_code_3, food_code_4, food_code_5, food_code_6, food_code_7, food_code_8, food_code_9, food_code_10) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                                (constituent_id, survey_answer[0], survey_answer[1], survey_answer[2], survey_answer[3], survey_answer[4], survey_answer[5], survey_answer[6], survey_answer[7], survey_answer[8], survey_answer[9]))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise
    
    def check(self, constituent_id: int) -> bool:
        """
        Check if a constituent has already answered the survey.

        Args:
            constituent_id (int): The identifier of the constituent to check.

        Returns:
            bool: True if the constituent has already answered the survey, False otherwise.
        """
        try:
            self.cursor.execute("SELECT constituent_id FROM survey WHERE constituent_id = %s", (constituent_id,))
            return True if self.cursor.fetchone() else False
        except Exception as e:
            print(e)
            raise
    
    def delete(self, constituent_id: int) -> bool:
        """
        Deletes a constituent's survey response from the database.

        Args:
            constituent_id (int): The identifier of the constituent whose survey response should be deleted.

        Returns:
            bool: True if the operation was successful, raises an exception otherwise.
        """
        try:
            self.cursor.execute("DELETE FROM survey WHERE constituent_id = %s", (constituent_id,))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise