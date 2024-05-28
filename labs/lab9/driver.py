import argparse

from crypto_mode import CryptoMode
from request import Request
from data_input_handler import DataInputHandler
from decryption_handler import DecryptionHandler
from encryption_handler import EncryptionHandler
from input_file_handler import InputFileHandler
from key_handler import KeyHandler
from output_handler import OutputHandler


class Crypto:
    def __init__(self):
        key_handler = KeyHandler()
        input_file_handler = InputFileHandler()
        data_input_handler = DataInputHandler()
        encryption_handler = EncryptionHandler()
        decryption_handler = DecryptionHandler()
        output_handler = OutputHandler()

        key_handler.set_next(input_file_handler)
        input_file_handler.set_next(data_input_handler)

        if request.encryption_state == CryptoMode.EN:
            data_input_handler.set_next(encryption_handler)
        elif request.encryption_state == CryptoMode.DE:
            data_input_handler.set_next(decryption_handler)

        encryption_handler.set_next(output_handler)
        decryption_handler.set_next(output_handler)

        self.encryption_start_handler = key_handler
        self.decryption_start_handler = key_handler

    def execute_request(self, req: Request):
        if req.encryption_state == CryptoMode.EN:
            self.encryption_start_handler.handle(req)
        elif req.encryption_state == CryptoMode.DE:
            self.decryption_start_handler.handle(req)


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


def main(request: Request):
    """
    The main function of the application. This function creates an
    object of type Crypto and calls the execute_request function on
    it.
    :param request: The object of type Request with all the arguments
    provided in it.
    """
    crypto = Crypto()
    crypto.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
