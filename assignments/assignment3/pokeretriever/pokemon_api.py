import aiohttp
from pokeretriever.pokemon import Pokemon
from pokeretriever.ability import Ability
from pokeretriever.move import Move
from pokeretriever.stat import Stat


class PokemonApi:
    @staticmethod
    async def fetch_data(url):
        """
        Fetches the data from the given url and returns the response.
        :param url: url to fetch data from
        :return: response
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.json()
        except (aiohttp.ClientError, Exception) as e:
            return e

    @staticmethod
    def parse_pokemon(data, entity_stat=None, entity_move=None, entity_ability=None):
        """
        Parses the data and returns a Pokémon object.
        :param data: data to parse
        :param entity_stat: entity_stat, a list of Stat objects to be used instead of parsing the data
        :param entity_move: entity_move, a list of Move objects to be used instead of parsing the data
        :param entity_ability: entity_ability, a list of Ability objects to be used instead of parsing the data
        :return: Pokémon object
        """
        pokemon = Pokemon(
            data["name"],
            data["id"],
            data["height"],
            data["weight"],
            {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
            if entity_stat is None
            else entity_stat,
            data["types"][0]["type"]["name"],
            [ability["ability"]["name"] for ability in data["abilities"]]
            if entity_ability is None
            else entity_ability,
            {
                move["move"]["name"]: move["version_group_details"][0][
                    "level_learned_at"
                ]
                for move in data["moves"]
            }
            if entity_move is None
            else entity_move,
        )
        return pokemon

    @staticmethod
    def parse_ability(data):
        """
        Parses the data and returns an Ability object.
        :param data: data to parse
        :return: Ability object
        """
        effect_en = None
        if len(data["effect_entries"]) > 0:
            for effect in data["effect_entries"]:
                if effect["language"]["name"] == "en":
                    effect_en = effect
                    break
        else:
            effect_en = {
                "effect": "N/A",
                "short_effect": "N/A",
            }

        return Ability(
            data["name"],
            data["id"],
            data["generation"]["name"],
            effect_en["effect"],
            effect_en["short_effect"],
            [pokemon["pokemon"]["name"] for pokemon in data["pokemon"]],
        )

    @staticmethod
    def parse_move(data):
        """
        Parses the data and returns a Move object.
        :param data: data to parse
        :return: Move object
        """
        effect_en = None
        if len(data["effect_entries"]) > 0:
            for effect in data["effect_entries"]:
                if effect["language"]["name"] == "en":
                    effect_en = effect
                    break
        else:
            effect_en = {
                "effect": "N/A",
                "short_effect": "N/A",
            }

        return Move(
            data["name"],
            data["id"],
            data["generation"]["name"],
            data["accuracy"],
            data["pp"],
            data["power"],
            data["type"]["name"],
            data["damage_class"]["name"],
            effect_en["short_effect"],
        )

    @staticmethod
    def parse_stat(data):
        """
        Parses the data and returns a Stat object.
        :param data: data to parse
        :return: Stat object
        """
        return Stat(
            data["name"],
            data["id"],
            data["is_battle_only"],
            "N/A"
            if data["move_damage_class"] is None
            else data["move_damage_class"]["name"],
        )
