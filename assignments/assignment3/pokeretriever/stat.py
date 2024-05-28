from pokedex_object import PokedexObject


class Stat(PokedexObject):
    def __init__(self, name, pokedex_id, is_battle_only, move_damage_class):
        """
        Initializes the attributes of the Stat class.
        :param name: String, the name of the stat
        :param pokedex_id: Integer, the id of the Pokédex
        :param is_battle_only: Boolean, the battle only status of the stat
        :param move_damage_class: String, the move damage class of the stat
        """
        super().__init__(name, pokedex_id)
        self.__is_battle_only = is_battle_only
        self.__move_damage_class = move_damage_class

    def get_is_battle_only(self):
        """
        Gets the battle only status of the stat.
        :return: Boolean, the battle only status of the stat
        """
        return self.__is_battle_only

    def set_is_battle_only(self, is_battle_only):
        """
        Sets the battle only status of the stat.
        :param is_battle_only: Boolean, the battle only status of the stat
        """
        self.__is_battle_only = is_battle_only

    def get_move_damage_class(self):
        """
        Gets the move damage class of the stat.
        :return: String, the move damage class of the stat
        """
        return self.__move_damage_class

    def set_move_damage_class(self, move_damage_class):
        """
        Sets the move damage class of the stat.
        :param move_damage_class: String, the move damage class of the stat
        """
        self.__move_damage_class = move_damage_class

    is_battle_only = property(get_is_battle_only, set_is_battle_only)
    move_damage_class = property(get_move_damage_class, set_move_damage_class)

    def __str__(self):
        """
        Returns the string representation of the stat.
        :return: String, the string representation of the stat
        """
        return (
            f"Name: {self.name}\n"
            f"ID: {self.pokedex_id}\n"
            f"Is_Battle_Only: {self.is_battle_only}\n"
            f"Move Damage Class: {self.move_damage_class}\n"
        )
