class Request:
    def __init__(self, mode, input_file, input_data, expanded, output_type):
        """
        Initializes a Request object with the given parameters.
        Contains all the information needed to make a Pokédex API request that
        is gathered by argparse from the command line.
        :param mode: String, the mode of the request (pokémon, ability, move)
        :param input_file: String, the name of the input file (if provided)
        :param input_data: String, the input data (if provided)
        :param expanded: Boolean, whether to expand the request or not
        :param output_type: String, the name of the output file (if provided)
        """
        self.__mode = mode
        self.__input_file = input_file
        self.__input_data = input_data
        self.__expanded = expanded
        self.__output_type = output_type

    def get_mode(self):
        """
        Gets the mode of the request.
        :return: String, the mode of the request
        """
        return self.__mode

    def set_mode(self, mode):
        """
        Sets the mode of the request.
        :param mode: String, the mode of the request
        """
        self.__mode = mode

    def get_input_file(self):
        """
        Gets the name of the input file.
        :return: String, the name of the input file
        """
        return self.__input_file

    def set_input_file(self, input_file):
        """
        Sets the name of the input file.
        :param input_file: String, the name of the input file
        """
        self.__input_file = input_file

    def get_input_data(self):
        """
        Gets the input data.
        :return: String, the input data
        """
        return self.__input_data

    def set_input_data(self, input_data):
        """
        Sets the input data.
        :param input_data: String, the input data
        """
        self.__input_data = input_data

    def get_expanded(self):
        """
        Gets whether to expand the request or not.
        :return: Boolean, whether to expand the request or not
        """
        return self.__expanded

    def set_expanded(self, expanded):
        """
        Sets whether to expand the request or not.
        :param expanded: Boolean, whether to expand the request or not
        """
        self.__expanded = expanded

    def get_output_type(self):
        """
        Gets the name of the output file.
        :return: String, the name of the output file
        """
        return self.__output_type

    def set_output_type(self, output_type):
        """
        Sets the name of the output file.
        :param output_type: String, the name of the output file
        """
        self.__output_type = output_type

    mode = property(get_mode, set_mode)
    input_file = property(get_input_file, set_input_file)
    input_data = property(get_input_data, set_input_data)
    expanded = property(get_expanded, set_expanded)
    output_type = property(get_output_type, set_output_type)

    def __str__(self):
        """
        Returns a string representation of the Request object.
        :return: String, a string representation of the Request object
        """
        return (
            f"Request\nmode: {self.__mode}\ninput_file: {self.__input_file}\ninput_data: {self.__input_data}\n"
            f"expanded: {self.__expanded}\noutput_type: {self.__output_type}\n"
        )
