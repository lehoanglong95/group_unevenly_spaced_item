from fastapi import APIRouter, Depends

from .dependency import get_usecase
from ..domain import (
    UnevenlySpacedItemsOutputDTO,
    UnevenlySpacedItemsInputDTO,
    UnevenlySpacedItemsUsecase,
)

router = APIRouter()

# Define an API endpoint
@router.post("/infer")
def infer(input: UnevenlySpacedItemsInputDTO,
          usecase: UnevenlySpacedItemsUsecase = Depends(get_usecase)) -> UnevenlySpacedItemsOutputDTO:
    return usecase.predict(input)
