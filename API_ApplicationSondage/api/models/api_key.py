from pydantic import BaseModel, Field

class APIKey(BaseModel):
    """
    APIKey Model class.

    Defines the structure of the 'APIKey' attribute with Pydantic validation.

    Attributes:
    - api_key_owner_id (int): The ID of the admin account that you want to manage an API key for.
    - api_key (str): The API key which you want to manage.
    """
    api_key_owner_id: int = Field(1,
                                  title="API Key Owner ID",
                                  description="The ID of the admin account which you want to manage an API key for")
    api_key: str = Field("b323afd64df64a98b44e83f19ac1e5d0",
                         title="API Key",
                         description="The API key which you want to manage")

class UpdateAPIKey(APIKey):
    """
    UpdateAPIKey Model class.

    Inherits from the 'APIKey' model and adds an additional attribute for the API key's active status.

    Attributes:
    - api_key_active (bool): The new active status of the API key.
    """
    api_key_active: bool = Field(True,
                                 title="API Key Active",
                                 description="The new active status of the API key")
