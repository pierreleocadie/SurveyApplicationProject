from pydantic import BaseModel, validator

class Survey(BaseModel):
    """
    Survey Model class.

    Defines the structure of a survey with Pydantic validation.
    Each survey includes 10 food items, identified by a unique food_code.
    The food_code should be greater than 0 and not exceed 3194.

    Attributes:
    - food_code_1 to food_code_10 (int): Each represents a food item chosen in the survey.
    """
    food_code_1: int 
    food_code_2: int
    food_code_3: int
    food_code_4: int
    food_code_5: int
    food_code_6: int
    food_code_7: int
    food_code_8: int
    food_code_9: int
    food_code_10: int

    @validator('food_code_1', 'food_code_2', 'food_code_3', 'food_code_4', 'food_code_5', 
               'food_code_6', 'food_code_7', 'food_code_8', 'food_code_9', 'food_code_10')
    def validate_food_code(cls, value):
        """
        Validates that the value of food_code is greater than 0 and not exceeding 3194.

        Args:
        - value (int): food_code value to validate.

        Raises:
        - ValueError: if value is not within the acceptable range.

        Returns:
        - int: validated value.
        """
        if value <= 0:
            raise ValueError('food_code should be greater than 0')
        if value > 3194:
            raise ValueError('food_code should not exceed 3194')
        return value
