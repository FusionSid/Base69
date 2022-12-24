import string

# things that will be imported when `from base69 import *`
__all__ = [
    "encode_base69_int",
    "encode_base69_text",
    "encode_base69_float",
    "decode_base69_int",
    "decode_base69_text",
    "decode_base69_float",
    "encode_base69",
    "InvalidInput",
]

BASE_69_PREFIX = "69*|"  # so it can be changed easily

# create conversion table
values = (
    list(string.digits)
    + list(string.ascii_uppercase)
    + list(string.ascii_lowercase)
    + ["+", "/", "=", "@", "*", "-", "!", "#"]
)
CONVERSION_TABLE = dict(zip(range(len(values)), values))


# custom exception that is raised when invalid input is provided
class InvalidInput(Exception):
    def __init__(self, message: str) -> None:
        message = f"Invalid input was provided! ({message})"
        super().__init__(message)


def encode_base69_int(input: int, *args: tuple, **kwargs: dict) -> str:
    """
    Encode an integer to Base69

    Parameters:
        input (`int`): The number to convert
        prefix (`Optional[bool]`): If true it will return text with the prefix

    Returns:
        `str`: The encoded Base69 result

    Raises:
        `InvalidInput`: If the input is invalid
    """

    if not type(input) == int:
        raise InvalidInput("Must be of type: int")

    base69 = ""
    while input > 0:
        remainder = input % 70
        base69 = CONVERSION_TABLE[remainder] + base69
        input = input // 70

    return BASE_69_PREFIX + base69 if kwargs.get("prefix", True) else base69


def decode_base69_int(input: str, *args: tuple, **kwargs: dict) -> int:
    """
    Decode Base69 text to an integer

    Parameters:
        input (`str`): the Base69 to decode

    Returns:
        `int`: The decoded integer result

    Raises:
        `InvalidInput`: If the input is invalid
    """

    if (
        not input.startswith(BASE_69_PREFIX)
        # user can choose to ignore the prefix warning with this kwarg
        and kwargs.get("ignore_prefix_warning", False) is False
    ):
        raise InvalidInput("Base69 must begin '69*|'")

    input = input[4:] if input.startswith(BASE_69_PREFIX) else input

    base = 0
    for i in range(len(input)):
        try:
            base += list(CONVERSION_TABLE.keys())[
                list(CONVERSION_TABLE.values()).index(input[i])
            ] * (70 ** (len(input) - i - 1))
        except ValueError as ve:
            invalid_char = ve.args[0].split(" ")[0]
            raise InvalidInput(f"{invalid_char} is not allowed")
    return base


def encode_base69_text(input: str) -> str:
    raise NotImplementedError


def encode_base69_float(input: float) -> str:
    raise NotImplementedError


def decode_base69_text(text: str) -> str:
    raise NotImplementedError


def decode_base69_float(text: str) -> float:
    raise NotImplementedError


def encode_base69(input: str | int | float, *args, **kwargs) -> str:
    functions = {
        int: encode_base69_int,
        str: encode_base69_text,
        float: encode_base69_float,
    }
    result = functions.get(type(input))
    if result is None:
        raise InvalidInput("Input must be of type int, float or string")

    return result(input, *args, *kwargs)
