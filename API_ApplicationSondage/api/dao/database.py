import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    """This class handles the connection to the MySQL database.

    It uses the connection details provided in the .env file.

    Attributes:
        db: A connection to the MySQL database.
    """

    def __init__(self) -> None:
        """Establishes a connection to the MySQL database.

        The database host, port, user, password, and name are all
        pulled from environment variables.
        """
        self.db = mysql.connector.connect(
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=os.getenv("DATABASE_NAME")
        )
    
    def get(self) -> mysql.connector:
        """Returns the current MySQL database connection.

        Returns:
            A mysql.connector object representing the connection to the database.
        """
        return self.db

if __name__ == "__main__":
    db = Database()
    cursor = db.get().cursor()
    cursor.execute("SELECT * FROM foods WHERE food_code = 1")
    result = cursor.fetchall()
    print(result)
    cursor.close()
    db.get().close()
