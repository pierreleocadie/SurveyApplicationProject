from .database import Database

class ApiKeyDAO:
    
    def __init__(self) -> None:
        """Initialise the ApiKey Data Access Object with a Database connection."""
        self.db = Database()
    
    def __enter__(self):
        """Open a new Database cursor when the object is entered using a with statement."""
        self.cursor = self.db.get().cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the Database cursor and connection when the object is exited."""
        self.cursor.close()
        self.db.get().close()
    
    def create(self, admin_id: int, api_key: str) -> bool:
        """Creates a new API key entry in the database.

        Args:
            admin_id: An integer of the admin's ID.
            api_key: A string of the API key.

        Returns:
            A boolean indicating if the operation was successful.
        """
        try:
            self.cursor.execute("INSERT INTO api_keys (api_key_owner_id, api_key) VALUES (%s, %s)", (admin_id, api_key,))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise
    
    def check_active(self, api_key: str) -> bool:
        """Checks if an API key is active in the database.

        Args:
            api_key: A string of the API key.

        Returns:
            A boolean indicating if the API key is active.
        """
        try:
            self.cursor.execute("SELECT * FROM api_keys WHERE api_key = %s AND active = 1", (api_key,))
            response = self.cursor.fetchone()
            if not response:
                return False
            return True
        except Exception as e:
            print(e)
            raise
    
    def check(self, api_key: str) -> bool:
        """Checks if an API key exists in the database.

        Args:
            api_key: A string of the API key.

        Returns:
            A boolean indicating if the API key exists.
        """
        try:
            self.cursor.execute("SELECT * FROM api_keys WHERE api_key = %s", (api_key,))
            response = self.cursor.fetchone()
            if not response:
                return False
            return True
        except Exception as e:
            print(e)
            raise
    
    def get_all(self) -> dict:
        """Retrieves all API key entries from the database.

        Returns:
            A list of dictionaries each representing an API key entry.
        """
        try:
            self.cursor.execute("SELECT * FROM api_keys")
            response = self.cursor.fetchall()
            if not response:
                raise Exception("No API Keys found")
            # Convert response to dict
            keys_data = []
            for key in response:
                key = dict(zip([x[0] for x in self.cursor.description], key))
                keys_data.append(key)
            return keys_data
        except Exception as e:
            print(e)
            raise
    
    def update(self, api_key_owner_id, api_key: str, active: bool) -> bool:
        """Updates an existing API key entry in the database.

        Args:
            api_key_owner_id: An integer of the admin's ID who owns the API key.
            api_key: A string of the API key.
            active: A boolean indicating if the API key should be active.

        Returns:
            A boolean indicating if the operation was successful.
        """
        try:
            self.cursor.execute("UPDATE api_keys SET active = %s WHERE api_key_owner_id = %s AND api_key = %s", (active, api_key_owner_id, api_key,))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise
    
    def delete(self, api_key: str) -> bool:
        """Deletes an API key entry from the database.

        Args:
            api_key: A string of the API key.

        Returns:
            A boolean indicating if the operation was successful.
        """
        try:
            self.cursor.execute("DELETE FROM api_keys WHERE api_key = %s", (api_key,))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise