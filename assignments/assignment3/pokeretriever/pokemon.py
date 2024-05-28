from pokedex_object import PokedexObject


class Pokemon(PokedexObject):
    def __init__(
        self,
        name,
        pokedex_id,
        height,
        weight,
        stats,
        types,
        abilities,
        moves,
    ):
        """
        Initializes the attributes of the Pokémon class.
        :param name: String, the name of the Pokémon
        :param pokedex_id: Integer, the id of the Pokédex
        :param height: Integer, the height of the Pokémon
        :param weight: Integer, the weight of the Pokémon
        :param stats: Stat dict, the stat names and base value of the Pokémon or list of Stat objects
        :param types: List of strings, the types of the moves
        :param abilities: Ability list, the ability names and URLs of the Pokémon or list of Ability objects
        :param moves: Move dict, the move names and levels of the moves or list of Move objects
        """
        super().__init__(name, pokedex_id)
        self.__height = height
        self.__weight = weight
        self.__stats = stats
        self.__types = types
        self.__abilities = abilities
        self.__moves = moves

    def get_height(self):
        """
        Gets the height of the Pokémon.
        :return: Integer, the height of the Pokémon
        """
        return self.__height

    def set_height(self, height):
        """
        Sets the height of the Pokémon.
        :param height: Integer, the height of the Pokémon
        """
        self.__height = height

    def get_weight(self):
        """
        Gets the weight of the Pokémon.
        :return: Integer, the weight of the Pokémon
        """
        return self.__weight

    def set_weight(self, weight):
        """
        Sets the weight of the Pokémon.
        :param weight: Integer, the weight of the Pokémon
        """
        self.__weight = weight

    def get_stats(self):
        """
        Gets the stats of the Pokémon.
        :return: Stat list, the stat names, base value, and URL of the Pokémon
        """
        return self.__stats

    def set_stats(self, stats):
        """
        Sets the stats of the Pokémon.
        :param stats: Stat list, the stat names, base value, and URL of the Pokémon
        """
        self.__stats = stats

    def get_types(self):
        """
        Gets the types of the Pokémon.
        :return: List of strings, the types of the Pokémon
        """
        return self.__types

    def set_types(self, types):
        """
        Sets the types of the Pokémon.
        :param types: List of strings, the types of the Pokémon
        """
        self.__types = types

    def get_abilities(self):
        """
        Gets the abilities of the Pokémon.
        :return: Ability list, the ability names and URLs of the Pokémon
        """
        return self.__abilities

    def set_abilities(self, abilities):
        """
        Sets the abilities of the Pokémon.
        :param abilities: Ability list, the ability names and URLs of the Pokémon
        """
        self.__abilities = abilities

    def get_moves(self):
        """
        Gets the moves of the Pokémon.
        :return: Move list, the move names of the Pokémon
        """
        return self.__moves

    def set_moves(self, moves):
        """
        Sets the moves of the Pokémon.
        :param moves: Move list, the move names of the Pokémon
        """
        self.__moves = moves

    height = property(get_height, set_height)
    weight = property(get_weight, set_weight)
    stats = property(get_stats, set_stats)
    types = property(get_types, set_types)
    abilities = property(get_abilities, set_abilities)
    moves = property(get_moves, set_moves)

    def __str__(self):
        """
        Returns a string representation of the Pokémon.
        :return: String, the string representation of the Pokémon
        """

        # If the request was expanded, the stats is a list of Stat objects.
        # If the request was not expanded, the stats is a dict of stat names and base values.
        if type(self.stats) is dict:
            stats_str = "\n".join(
                [
                    f"('{stat_name}', {stat_value})"
                    for stat_name, stat_value in self.stats.items()
                ]
            )
        else:
            stats_str = "\n".join([f"{stat_item}" for stat_item in self.stats])

        abilities_str = "\n".join([f"{ability}" for ability in self.abilities])

        # If the request was expanded, the moves is a list of Move objects.
        # If the request was not expanded, the moves is a dict of move names and levels.
        if type(self.moves) is dict:
            moves_str = "\n\n".join(
                [
                    f"('Move name: {move_name}', 'Level acquired: {move_level}')"
                    for move_name, move_level in self.moves.items()
                ]
            )
        else:
            moves_str = "\n\n".join([f"{move}" for move in self.moves])

        return (
            f"Name: {self.name}\n"
            f"ID: {self.pokedex_id}\n"
            f"Height: {self.height}\n"
            f"Weight: {self.weight}\n"
            f"Types: {self.types}\n\n"
            f"Stats:\n------\n\n{stats_str}\n"
            f"Abilities:\n------\n\n{abilities_str}\n\n"
            f"Moves:\n------\n\n{moves_str}"
        )
