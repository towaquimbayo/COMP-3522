class PokedexObject:
    def __init__(self, name, pokedex_id):
        """
        Initializes the attributes of the PokedexObject class.
        Base class that defines the name and id parameter for
        Pokémon, Ability, Move, and Stat classes.
        :param name: String, the name of the Pokémon
        :param pokedex_id: Integer, the id of the Pokédex
        """
        self.__name = name
        self.__id = pokedex_id

    def get_name(self):
        """
        Getter method for the name attribute.
        :return: String, the name of the Pokémon
        """
        return self.__name

    def set_name(self, name):
        """
        Setter method for the name attribute.
        :param name: String, the name of the Pokémon
        """
        self.__name = name

    def get_id(self):
        """
        Getter method for the id attribute.
        :return: Integer, the id of the Pokédex
        """
        return self.__id

    def set_id(self, pokedex_id):
        """
        Setter method for the id attribute.
        :param pokedex_id: Integer, the id of the Pokédex
        """
        self.__id = pokedex_id

    name = property(get_name, set_name)
    pokedex_id = property(get_id, set_id)
