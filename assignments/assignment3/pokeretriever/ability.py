from pokedex_object import PokedexObject


class Ability(PokedexObject):
    def __init__(self, name, pokedex_id, generation, effect, short_effect, pokemon):
        """
        Initializes the attributes of the Ability class.
        :param name: String, the name of the ability
        :param pokedex_id: Integer, the id of the Pokédex
        :param generation: String, the generation of the Pokémon
        :param effect: String, the effect of the ability
        :param short_effect: String, the short effect of the ability
        :param pokemon: List of strings, the pokémon names that have the ability
        """
        super().__init__(name, pokedex_id)
        self.__generation = generation
        self.__effect = effect
        self.__short_effect = short_effect
        self.__pokemon_list = pokemon

    def get_generation(self):
        """
        Returns the generation of the ability
        :return: String, the generation of the ability
        """
        return self.__generation

    def set_generation(self, generation):
        """
        Sets the generation of the ability
        :param generation: String, the generation of the ability
        """
        self.__generation = generation

    def get_effect(self):
        """
        Returns the effect of the ability
        :return: String, the effect of the ability
        """
        return self.__effect

    def set_effect(self, effect):
        """
        Sets the effect of the ability
        :param effect: String, the effect of the ability
        """
        self.__effect = effect

    def get_short_effect(self):
        """
        Returns the short effect of the ability
        :return: String, the short effect of the ability
        """
        return self.__short_effect

    def set_short_effect(self, short_effect):
        """
        Sets the short effect of the ability
        :param short_effect: String, the short effect of the ability
        """
        self.__short_effect = short_effect

    def get_pokemon_list(self):
        """
        Returns the list of pokémon that have the ability
        :return: List of strings, the list of pokémon that have the ability
        """
        return self.__pokemon_list

    def set_pokemon_list(self, pokemon_list):
        """
        Sets the list of pokémon that have the ability
        :param pokemon_list: List of strings, the list of pokémon that have the ability
        """
        self.__pokemon_list = pokemon_list

    generation = property(get_generation, set_generation)
    effect = property(get_effect, set_effect)
    short_effect = property(get_short_effect, set_short_effect)
    pokemon_list = property(get_pokemon_list, set_pokemon_list)

    def __str__(self):
        """
        Returns the string representation of the Ability class
        :return: String, the string representation of the Ability class
        """
        return (
            f"Name: {self.name}\n"
            f"ID: {self.pokedex_id}\n"
            f"Generation: {self.generation}\n"
            f"Effect: {self.effect}\n"
            f"Effect (Short): {self.short_effect}\n"
            f"Pokemon: {', '.join(self.pokemon_list)}\n"
        )
