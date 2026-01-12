from abc import ABC, abstractmethod
from typing import List
import pandas as pd

from rail_validation.models import ValidationIssue


class ValidationRule(ABC):
    """
    Base class for all validation rules.
    Each rule must implement a name and a validate method.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def validate(self, df: pd.DataFrame) -> List[ValidationIssue]:
        """
        Execute the validation rule on the given dataframe.
        Returns a list of ValidationIssue objects.
        """
        pass
