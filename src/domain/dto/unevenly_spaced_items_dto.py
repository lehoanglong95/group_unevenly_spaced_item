from pydantic import BaseModel
from typing import List

class UnevenlySpacedItemsInput(BaseModel):
    input: List
    direction: str

class UnevenlySpacedItemsOutput(BaseModel):
    output: List
