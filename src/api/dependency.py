from fastapi import Depends
from ..domain import (
    UnevenlySpacedItemsUsecase,
    UnevenlySpacedItemsHorizontalPredictor,
    UnevenlySpacedItemsVerticalPredictor,
)
from ..infrastructure import(
    UnevenlySpacedItemsHorizontalPredictorImpl,
    UnevenlySpacedItemsVerticalPredictorImpl,
)


def get_horizontal_predictor() -> UnevenlySpacedItemsHorizontalPredictor:
    return UnevenlySpacedItemsHorizontalPredictorImpl()


def get_vertical_predictor() -> UnevenlySpacedItemsVerticalPredictor:
    return UnevenlySpacedItemsVerticalPredictorImpl()


def get_usecase(horizontal_predictor=Depends(get_horizontal_predictor),
                vertical_predictor=Depends(get_vertical_predictor)) -> UnevenlySpacedItemsUsecase:
    return UnevenlySpacedItemsUsecase(horizontal_predictor, vertical_predictor)
