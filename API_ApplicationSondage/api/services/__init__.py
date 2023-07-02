"""
The services package provides various services for managing administrative tasks, API keys, constituents, food data, surveys, and statistics.

Sub-packages:
- admin: Sub-package for administrative tasks.
- api_key: Sub-package for managing API keys.
- constituent: Sub-package for managing constituent data.
- food: Sub-package for managing food data.
- survey: Sub-package for managing survey answers.
- stats: Sub-package for generating statistical data.

Note: Each sub-package contains multiple modules providing specific functionalities.
"""
from .admin import *
from .api_key import *
from .constituent import *
from .food import *
from .survey import *
from .stats import *
