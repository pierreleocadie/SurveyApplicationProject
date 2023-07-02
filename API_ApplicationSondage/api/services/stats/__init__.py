"""
The `stats` sub-package provides classes for retrieving statistical information about food consumption.

Sub-modules:
- `get_most_consumed_foods_by_age_group`: Class for retrieving the most consumed foods by age group.
- `get_most_consumed_food_groups_by_age_group`: Class for retrieving the most consumed food groups by age group.
- `get_most_consumed_food_subgroups_by_age_group`: Class for retrieving the most consumed food subgroups by age group.
- `get_most_consumed_food_sub_subgroups_by_age_group`: Class for retrieving the most consumed food sub-subgroups by age group.
"""
from .get_most_consumed_foods_by_age_group import GetMostConsumedFoodsByAgeGroup
from .get_most_consumed_food_groups_by_age_group import GetMostConsumedGroupsByAgeGroup
from .get_most_consumed_food_subgroups_by_age_group import GetMostConsumedSubgroupsByAgeGroup
from .get_most_consumed_food_sub_subgroups_by_age_group import GetMostConsumedSubSubgroupsByAgeGroup
