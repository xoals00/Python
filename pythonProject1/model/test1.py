from pydantic import BaseModel
from typing import List

class TierInfo(BaseModel):
    queue : str = ''
    tier : str = ''
    division : str = ''
    lp : int = 0

class TierCheck(BaseModel):
    queue: str = ''
    tier: str = ''
    division: str = ''
    lp: int = 0

class TierInput(BaseModel):
    queue: str = ''
    tier: str = ''
    division: str = ''
    lp: int = 0

class TierListInfo(BaseModel):
    total_tier_list : List[TierInfo] = []

class TierListCheck(BaseModel):
    total_tiercheck_list : List[TierCheck] = []

class TierListInput(BaseModel):
    total_tier_list_input : List[TierInput] = []