from dao import ConstituentDAO

class Register:
    """Class for registering a constituent."""
    
    def __init__(self, last_name: str, first_name: str, birth: str, address: str, postal_code: str, city: str, phone: str) -> None:
        """
        Initialize a Register instance.
        
        Args:
            last_name (str): The last name of the constituent.
            first_name (str): The first name of the constituent.
            birth (str): The birth date of the constituent.
            address (str): The address of the constituent.
            postal_code (str): The postal code of the constituent.
            city (str): The city of the constituent.
            phone (str): The phone number of the constituent.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth = birth
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.phone = phone
        self.response = self.__register()
    
    def __register(self) -> dict:
        """
        Register a constituent.
        
        Returns:
            dict: A dictionary containing the response of the operation.
                If successful, the dictionary will have a "success" key with a message and the constituent ID.
                If unsuccessful, the dictionary will have an "error" key with a message.
        """
        try:
            with ConstituentDAO() as constituent_dao:
                constituent_dao.register(self.last_name, self.first_name, self.birth, self.address, self.postal_code, self.city, self.phone)
                response = constituent_dao.get_id(self.last_name, self.first_name, self.birth, self.address, self.postal_code, self.city, self.phone)
            return {"success": "Constituent registered", "id": response["constituent_id"]}
        except Exception as e:
            print(e)
            return {"error": "Failed to register constituent"}
    
    def get_response(self) -> dict:
        """
        Get the response of the constituent registration.
        
        Returns:
            dict: A dictionary containing the response of the constituent registration.
        """
        return self.response
