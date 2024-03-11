from typing import List
import joblib
from pandas import DataFrame

from ..domain import (
    UnevenlySpacedItemsHorizontalPredictor,
    UnevenlySpacedItemsVerticalPredictor,
)


class UnevenlySpacedItemsHorizontalPredictorImpl(UnevenlySpacedItemsHorizontalPredictor):

    def __init__(self):
        self.model = joblib.load("data_analyst/horizontal_decision_tree_model.pkl")

    def predict(self, input_list: DataFrame) -> List:
        return self.model.predict(input_list)


class UnevenlySpacedItemsVerticalPredictorImpl(UnevenlySpacedItemsVerticalPredictor):

    def __init__(self):
        self.model = joblib.load("data_analyst/horizontal_decision_tree_model.pkl")

    def predict(self, input_list: DataFrame) -> List:
        return self.model.predict(input_list)