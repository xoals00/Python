import requests
from model.test1 import *


def get_tier_check(queue, tier, division, lp) -> TierCheck:
    return TierCheck(
        queue=queue,
        tier=tier,
        division=division,
        lp=lp

    )


def get_tier(queue, tier, division, lp) -> TierInfo:
    return TierInfo(
        queue=queue,
        tier=tier,
        division=division,
        lp=lp
    )
def get_list_input() -> TierInput:
    return TierInput(

    )


def test(riot_id: str,
         tag: str
         ) -> TierListInfo:
    api_key = 'RGAPI-f94a4128-cb3b-4303-b92b-0016fa59b5a8'
    url1 = f'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tag}?api_key={api_key}'
    res1 = requests.get(url1).json()
    puu_id = res1['puuid']
    url2 = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puu_id}?api_key={api_key}'
    res2 = requests.get(url2).json()
    summoner_id = res2['id']
    url3 = f'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}'
    res3 = requests.get(url3).json()

    tier_list = []
    for league in res3:
        if league['queueType'] == 'RANKED_SOLO_5x5':
            queue = league['queueType']
            solo_rank_tier = league['tier']
            solo_rank_division = league['rank']
            solo_rank_lp = league['leaguePoints']
            tier = get_tier(queue, solo_rank_tier, solo_rank_division, solo_rank_lp)
            tier_list.append(tier)
        elif league['queueType'] == 'RANKED_FLEX_SR':
            queue = league['queueType']
            flex_rank_tier = league['tier']
            flex_rank_division = league['rank']
            flex_rank_lp = league['leaguePoints']
            tier = get_tier(queue, flex_rank_tier, flex_rank_division, flex_rank_lp)
            tier_list.append(tier)
    return TierListInfo(
        total_tier_list=tier_list
    )


def tier_check_test(tier: str,
                    division: str
                    ) -> TierListCheck:
    print("hi")

    api_key = 'RGAPI-f94a4128-cb3b-4303-b92b-0016fa59b5a8'
    url = f'https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{division}?page=1&api_key={api_key}'
    res = requests.get(url).json()
    a = []
    for i in range(0, 5):
        queue = res[i]['queueType']
        solo_rank_tier = res[i]['tier']
        solo_rank_division = res[i]['rank']
        solo_rank_lp = res[i]['leaguePoints']
        tier_check = get_tier_check(queue,solo_rank_tier,solo_rank_division,solo_rank_lp)
        a.append(tier_check)
    # print(a)
    return TierListCheck(
        total_tiercheck_list=a
    )

def lol_data_input(riot_id: str,
         tag: str
         ) -> TierListInput:
    api_key = 'RGAPI-f94a4128-cb3b-4303-b92b-0016fa59b5a8'
    url1 = f'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tag}?api_key={api_key}'
    res1 = requests.get(url1).json()
    puu_id = res1['puuid']

    url2 = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start=0&count=20&api_key={api_key}"
    res2 = requests.get(url2).json()
    match_id = res2

    url3 = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    res3 = requests.get(url3).json()
    match_data = res3
