from pokedex_object import PokedexObject


class Move(PokedexObject):
    def __init__(
        self,
        name,
        pokedex_id,
        generation,
        accuracy,
        pp,
        power,
        move_type,
        damage_class,
        short_effect,
    ):
        """
        Initializes the attributes of the Move class.
        :param name: String, the name of the move
        :param pokedex_id: Integer, the id of the Pokédex
        :param generation: String, the generation of the move
        :param accuracy: Integer, the accuracy of the move
        :param pp: Integer, the pp of the move
        :param power: Integer, the power of the move
        :param move_type: String, the type of the move
        :param damage_class: String, the damage class of the move
        :param short_effect: String, the short effect of the move
        """
        super().__init__(name, pokedex_id)
        self.__generation = generation
        self.__accuracy = accuracy
        self.__pp = pp
        self.__power = power
        self.__type = move_type
        self.__damage_class = damage_class
        self.__short_effect = short_effect

    def get_generation(self):
        """
        Returns the generation of the move.
        :return: String, the generation of the move
        """
        return self.__generation

    def set_generation(self, generation):
        """
        Sets the generation of the move.
        :param generation: String, the generation of the move
        """
        self.__generation = generation

    def get_accuracy(self):
        """
        Returns the accuracy of the move.
        :return: Integer, the accuracy of the move
        """
        return self.__accuracy

    def set_accuracy(self, accuracy):
        """
        Sets the accuracy of the move.
        :param accuracy: Integer, the accuracy of the move
        """
        self.__accuracy = accuracy

    def get_pp(self):
        """
        Returns the pp of the move.
        :return: Integer, the pp of the move
        """
        return self.__pp

    def set_pp(self, pp):
        """
        Sets the pp of the move.
        :param pp: Integer, the pp of the move
        """
        self.__pp = pp

    def get_power(self):
        """
        Returns the power of the move.
        :return: Integer, the power of the move
        """
        return self.__power

    def set_power(self, power):
        """
        Sets the power of the move.
        :param power: Integer, the power of the move
        """
        self.__power = power

    def get_type(self):
        """
        Returns the type of the move.
        :return: String, the type of the move
        """
        return self.__type

    def set_type(self, move_type):
        """
        Sets the type of the move.
        :param move_type: String, the type of the move
        """
        self.__type = move_type

    def get_damage_class(self):
        """
        Returns the damage class of the move.
        :return: damage_class: String, the damage class of the move
        """
        return self.__damage_class

    def set_damage_class(self, damage_class):
        """
        Sets the damage class of the move.
        :param damage_class: String, the damage class of the move
        """
        self.__damage_class = damage_class

    def get_short_effect(self):
        """
        Returns the short effect of the move.
        :return: String, the short effect of the move
        """
        return self.__short_effect

    def set_short_effect(self, short_effect):
        """
        Sets the short effect of the move.
        :param short_effect: String, the short effect of the move
        """
        self.__short_effect = short_effect

    generation = property(get_generation, set_generation)
    accuracy = property(get_accuracy, set_accuracy)
    pp = property(get_pp, set_pp)
    power = property(get_power, set_power)
    type = property(get_type, set_type)
    damage_class = property(get_damage_class, set_damage_class)
    short_effect = property(get_short_effect, set_short_effect)

    def __str__(self):
        """
        Returns the string representation of the Move class.
        :return: String, the string representation of the Move class
        """
        return (
            f"Name: {self.name}\n"
            f"Id: {self.pokedex_id}\n"
            f"Generation: {self.generation}\n"
            f"Accuracy: {self.accuracy}\n"
            f"PP: {self.pp}\n"
            f"Power: {self.power}\n"
            f"Type: {self.type}\n"
            f"Damage Class: {self.damage_class}\n"
            f"Effect (Short): {self.short_effect}\n"
        )
