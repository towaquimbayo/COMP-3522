from enum import Enum


class ApiEndpoints(Enum):
    BASE_URL = "https://pokeapi.co/api/v2/"
    ABILITY = f"{BASE_URL}ability/{{}}/"
    MOVE = f"{BASE_URL}move/{{}}/"
    POKEMON = f"{BASE_URL}pokemon/{{}}/"
