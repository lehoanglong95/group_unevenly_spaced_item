from typing import List
from abc import ABC, abstractmethod
from pandas import DataFrame

class UnevenlySpacedItemsHorizontalPredictor(ABC):

    @abstractmethod
    def predict(self, input_list: DataFrame) -> List:
        pass

class UnevenlySpacedItemsVerticalPredictor(ABC):

    @abstractmethod
    def predict(self, input_list: DataFrame) -> List:
        pass
