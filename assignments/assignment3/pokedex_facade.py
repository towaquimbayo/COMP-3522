import asyncio
import argparse
from time import time
from datetime import datetime
from pathlib import Path
from enums.pokedex_mode import PokedexMode
from enums.api_endpoints import ApiEndpoints
from request import Request
from pokeretriever.pokemon_api import PokemonApi


class PokedexFacade:
    @staticmethod
    def get_request_from_args():
        """
        Gets the request from the command line arguments and parse using argparse.
        :return: Request, the request object
        :raises: Exception, if the request object cannot be instantiated
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "mode",
            choices=["pokemon", "ability", "move"],
            help="The mode to use to set the Pokedex. It can be {'pokemon' | 'ability' | 'move'}",
        )
        parser.add_argument(
            "--inputfile",
            help="The inputfile is used pass inputs to the program. Input file has to be .txt format.",
        )
        parser.add_argument(
            "--inputdata",
            help="The inputdata is used to pass inputs to the program. These arguments are name and id. "
            "Note: Input data has to be a String.",
        )
        parser.add_argument(
            "--expanded",
            action="store_const",
            const=True,
            help="When this is provided a certain attributes are expanded.",
        )
        parser.add_argument(
            "--output",
            default=None,
            help="When this provided with filename and .txt extension, then the output will printed to specified "
            "textfile. If it is not provided it will be logged to the console.",
        )

        args = parser.parse_args()
        try:
            request = Request(
                args.mode.lower(),
                args.inputfile,
                [args.inputdata] if args.inputdata is not None else None,
                args.expanded,
                args.output,
            )
            return request
        except Exception as e:
            raise e

    @staticmethod
    def read_input_file(file_path):
        """
        Reads the input file and returns a list of names or ids.
        :param file_path: file path of the input file
        :return: list of names or ids
        """
        try:
            if not Path(file_path).exists():
                raise FileNotFoundError("Input file not found.")
            if not Path(file_path).is_file():
                raise TypeError("Input file is not a file.")
            if Path(file_path).suffix[1:] != "txt":
                raise TypeError("Input file is not a .txt file.")
            if Path(file_path).stat().st_size == 0:
                raise ValueError("Input file is empty.")
            with open(file_path, "r") as file:
                return [name_or_id.strip() for name_or_id in file]
        except (FileNotFoundError, TypeError, ValueError) as e:
            raise e
        except Exception as e:
            raise Exception(f"Error reading the input file.\nError: {e}")

    @staticmethod
    def get_data(file_path, input_data):
        """
        Gets the data from the input file or input data and returns a list of names or ids.
        :param file_path: file path of the input file if provided
        :param input_data: input data if provided
        :return: list of names or ids
        """
        if file_path is not None:
            return PokedexFacade.read_input_file(file_path)
        elif input_data is not None:
            return input_data
        else:
            raise ValueError("No input data or input file provided.")

    @staticmethod
    def create_entities(mode, data_entities, entities_expanded):
        """
        Creates the entities based on the mode.
        :param mode: PokedexMode enum value, either POKÉMON, ABILITY or MOVE
        :param data_entities: list of data entities
        :param entities_expanded: list of expanded data entities
        :return: list of entities
        """
        try:
            parser_function = getattr(PokemonApi, f"parse_{mode.lower()}")
            entities = []

            for i, data_entity in enumerate(data_entities):
                try:
                    if mode == PokedexMode.POKEMON.value:
                        entities.append(
                            parser_function(
                                data_entity,
                                None
                                if entities_expanded is None
                                else entities_expanded[i]["entity_stat"],
                                None
                                if entities_expanded is None
                                else entities_expanded[i]["entity_move"],
                                None
                                if entities_expanded is None
                                else entities_expanded[i]["entity_ability"],
                            )
                        )
                    else:
                        entities.append(parser_function(data_entity))
                except TypeError:
                    entities.append(f"\nAn error occurred. Skipping this request.")
            return entities
        except AttributeError:
            raise ValueError("Invalid mode.")
        except Exception as e:
            raise e

    @staticmethod
    async def execute_request(request: Request):
        """
        Processes the request and creates the entities based on the mode.
        :param request: request object containing the mode, input file, input data, expanded and output type
        :return: list of entities
        """
        try:
            data = PokedexFacade.get_data(request.input_file, request.input_data)
        except Exception as e:
            raise e

        try:
            entities = []

            url = ApiEndpoints[request.mode.upper()].value
            coroutines = [
                PokemonApi.fetch_data(url.format(name_or_id)) for name_or_id in data
            ]
            responses = await asyncio.gather(*coroutines)

            if request.expanded and request.mode == PokedexMode.POKEMON.value:
                entities.extend(await PokedexFacade.fetch_expanded_entities(responses))
        except ValueError as e:
            raise e
        except Exception as e:
            raise e

        return PokedexFacade.create_entities(
            request.mode,
            responses,
            entities if len(entities) > 0 else None,
        )

    @staticmethod
    async def fetch_expanded_entities(responses):
        """
        Fetches the expanded entities based on the responses and returns a list of expanded entities.
        :param responses: list of responses
        :return: list of expanded entities
        """
        expanded_entities = []

        for response in responses:
            if isinstance(response, str):
                continue

            stats_coroutines = [
                PokemonApi.fetch_data(stat["stat"]["url"]) for stat in response["stats"]
            ]
            moves_coroutines = [
                PokemonApi.fetch_data(move["move"]["url"]) for move in response["moves"]
            ]
            abilities_coroutines = [
                PokemonApi.fetch_data(ability["ability"]["url"])
                for ability in response["abilities"]
            ]

            (
                stats_responses,
                moves_responses,
                abilities_responses,
            ) = await asyncio.gather(
                asyncio.gather(*stats_coroutines),
                asyncio.gather(*moves_coroutines),
                asyncio.gather(*abilities_coroutines),
            )

            entity_stat = [PokemonApi.parse_stat(stat) for stat in stats_responses]
            entity_move = [PokemonApi.parse_move(move) for move in moves_responses]
            entity_ability = [
                PokemonApi.parse_ability(ability) for ability in abilities_responses
            ]

            expanded_entities.append(
                {
                    "entity_stat": entity_stat,
                    "entity_move": entity_move,
                    "entity_ability": entity_ability,
                }
            )
        return expanded_entities

    @staticmethod
    def create_report(entities, output_type):
        """
        Creates the report based on the entities and output type.
        :param entities: list of entities
        :param output_type: output type, either None or a file path
        """
        report = (
            f"Timestamp: {datetime.fromtimestamp(time()).strftime('%d/%m/%Y %H:%M')}\n"
        )
        report += f"Number of requests: {len(entities)}"

        if output_type is not None:
            with open(output_type, "w", encoding="UTF-8") as file:
                file.write(report)
                for item in entities:
                    file.write("\n" + str(item))
        else:
            print(report)
            for item in entities:
                print(item)
