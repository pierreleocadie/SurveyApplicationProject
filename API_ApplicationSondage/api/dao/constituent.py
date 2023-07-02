from .database import Database

class ConstituentDAO:
    
    def __init__(self) -> None:
        """Initialise the Constituent Data Access Object with a Database connection."""
        self.db = Database()
    
    def __enter__(self):
        """Open a new Database cursor when the object is entered using a with statement."""
        self.cursor = self.db.get().cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the Database cursor and connection when the object is exited."""
        self.cursor.close()
        self.db.get().close()
    
    def get(self, constituent_id: int) -> bool:
        """Retrieves a constituent entry from the database based on its ID.

        Args:
            constituent_id: An integer of the constituent's ID.

        Returns:
            A boolean indicating if the constituent was found.
        """
        try:
            self.cursor.execute("SELECT * FROM constituents WHERE constituent_id = %s", (constituent_id,))
            return True if self.cursor.fetchone() else False
        except Exception as e:
            print(e)
            raise
    
    def register(self, last_name: str, first_name: str, birth: str, address: str, postal_code: str, city: str, phone: str) -> bool:
        """Registers a new constituent entry in the database.

        Args:
            last_name: A string of the constituent's last name.
            first_name: A string of the constituent's first name.
            birth: A string of the constituent's date of birth.
            address: A string of the constituent's address.
            postal_code: A string of the constituent's postal code.
            city: A string of the constituent's city.
            phone: A string of the constituent's phone number.

        Returns:
            A boolean indicating if the registration was successful.
        """
        try:
            self.cursor.execute("INSERT INTO constituents (last_name, first_name, birth, address, postal_code, city, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)", (last_name, first_name, birth, address, postal_code, city, phone,))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise
    
    def get_id(self, last_name: str, first_name: str, birth: str, address: str, postal_code: str, city: str, phone: str) -> dict:
        """Retrieves the ID of a constituent based on their personal details.

        Args:
            last_name: A string of the constituent's last name.
            first_name: A string of the constituent's first name.
            birth: A string of the constituent's date of birth.
            address: A string of the constituent's address.
            postal_code: A string of the constituent's postal code.
            city: A string of the constituent's city.
            phone: A string of the constituent's phone number.

        Returns:
            A dictionary with the constituent's ID if found.
        """
        try:
            self.cursor.execute("SELECT constituent_id FROM constituents WHERE last_name = %s AND first_name = %s AND birth = %s AND address = %s AND postal_code = %s AND city = %s AND phone = %s", (last_name, first_name, birth, address, postal_code, city, phone,))
            response = self.cursor.fetchone()
            return dict(zip([x[0] for x in self.cursor.description], response))
        except Exception as e:
            print(e)
            raise
    
    def delete(self, constituent_id: int) -> bool:
        """Deletes a constituent entry from the database.

        Args:
            constituent_id: An integer of the constituent's ID.

        Returns:
            A boolean indicating if the operation was successful.
        """
        try:
            self.cursor.execute("DELETE FROM constituents WHERE constituent_id = %s", (constituent_id,))
            self.db.get().commit()
            return True
        except Exception as e:
            print(e)
            raise
