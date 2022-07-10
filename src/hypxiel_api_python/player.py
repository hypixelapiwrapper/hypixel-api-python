from src.hypxiel_api_python.utils.requests import get
from math import sqrt


class HypixelPlayer:
    def __init__(self):
        pass

    async def network_level(self):
        player = await get(endpoint="player")
        network_experience = player["player"]["networkExp"] if "networkExp" in player["player"] else 0
        network_level = (sqrt((2 * network_experience) + 30625) / 50) - 2.5 if network_experience != 0 else 1
        return network_level