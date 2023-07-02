from pydantic import BaseModel, Field

class Constituent(BaseModel):
    """
    Constituent Model class.

    Defines the structure of a Constituent's details with Pydantic validation.

    Attributes:
    - last_name (str): Last name of the constituent.
    - first_name (str): First name of the constituent.
    - birth (str): Date of birth of the constituent in the format YYYY/MM/DD.
    - address (str): Address of the constituent.
    - postal_code (str): Postal code of the constituent.
    - city (str): City of the constituent.
    - phone (str): Phone number of the constituent.
    """
    last_name: str = Field("Dupont",
                     title="Last name",
                     description="Last name of the constituent",
                     min_length=2)
    first_name: str = Field("Jean",
                        title="First name",
                        description="First name of the constituent",
                        min_length=2)
    birth: str = Field("1990/01/01", 
                            title="Birth date",
                            description="Date of birth of the constituent in the format YYYY/MM/DD",
                            regex="^([0-9]{4})/([0-9]{2})/([0-9]{2})$")
    address: str = Field("1 rue de la Paix",
                         title="Address",
                         description="Address of the constituent",
                         min_length=5,
                         max_length=50)
    postal_code: str = Field("75000",
                            title="Postal code",
                            description="Postal code of the constituent",
                            regex="^([0-9]{5})$")
    city: str = Field("Paris",
                          title="City",
                         description="City of the constituent",
                         min_length=2)
    phone: str = Field("0123456789",
                     title="Phone",
                     description="Phone number of the constituent",
                     regex="^([0-9]{10})$")
