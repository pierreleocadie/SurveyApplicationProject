import bcrypt
from .database import Database

class AdminDAO:

    def __init__(self) -> None:
        """Initialise the Admin Data Access Object with a Database connection."""
        self.db = Database()
    
    def __enter__(self):
        """Open a new Database cursor when the object is entered using a with statement."""
        self.cursor = self.db.get().cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the Database cursor and connection when the object is exited."""
        self.cursor.close()
        self.db.get().close()
    
    def hash_password(self, password: str) -> str:
        """Hashes a given password using bcrypt.
        
        Args:
            password: A string of the password to hash.

        Returns:
            A hashed version of the password.
        """
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    
    def create(self, username: str, password: str, role: str) -> bool:
        """Creates a new admin entry in the database.

        Args:
            username: A string of the admin's username.
            password: A string of the admin's password.
            role: A string of the admin's role.

        Returns:
            A boolean indicating if the operation was successful.
        """
        password = self.hash_password(password)
        try:
            self.cursor.execute("INSERT INTO admin (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise
    
    def get(self, admin_id: int = None, username: str = None) -> bool | dict:
        """Retrieves an admin entry from the database based on ID or username.

        Args:
            admin_id: An integer of the admin's ID.
            username: A string of the admin's username.

        Returns:
            A boolean False if no matching entry is found, else a dictionary of the admin entry.
        """
        try:
            self.cursor.execute("SELECT * FROM admin WHERE admin_id = %s OR username = %s", (admin_id, username,))
            response = self.cursor.fetchone()
            if not response:
                return False
            # Convert response to dict
            rowHeaders = [x[0] for x in self.cursor.description]
            response = dict(zip(rowHeaders, response))
            return response
        except Exception as e:
            print(e)
            raise
    
    def update(self, username: str, password: str, role: str) -> bool:
        """Updates an existing admin entry in the database.

        Args:
            username: A string of the admin's username.
            password: A string of the admin's new password.
            role: A string of the admin's new role.

        Returns:
            A boolean indicating if the operation was successful.
        """
        password = self.hash_password(password)
        try:
            self.cursor.execute("UPDATE admin SET password = %s, role = %s WHERE username = %s", (password, role, username))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise
    
    def delete(self, username: str) -> bool:
        """Deletes an admin entry from the database.

        Args:
            username: A string of the admin's username.

        Returns:
            A boolean indicating if the operation was successful.
        """
        try:
            self.cursor.execute("DELETE FROM admin WHERE username = %s", (username,))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise