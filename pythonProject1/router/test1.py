from code22.test1 import *
from model.test1 import *
from fastapi import *

router = APIRouter(prefix='/summoner')


@router.get(
    path='/tier',
    response_model=TierListInfo
)
def summoner_tier(
        riot_id: str,
        tag: str
) -> TierListInfo:
    return test(riot_id, tag)


@router.get(
    path='/tiercheck',
    response_model=TierListCheck
)
def summoner_tier_check(
        tier: str,
        division: str
) -> TierListCheck:
    print("성공")
    return tier_check_test(tier, division)

@router.get(
    path="loldatainput",
    response_model=TierListInput

)
def summoner_tier_input(
        riot_id: str,
        tag: str
) -> TierListInput:
    return lol_data_input(riot_id, tag)