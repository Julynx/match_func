"""
@file     match_func.py
@brief    Pattern matching as a function.
@date     20/07/2023
@author   Julio Cabria
"""


def match(variable, dictionary, *, default=None):
    """
    Returns the first value from 'dictionary' whose key matches 'variable'.

    Usage:
        match(20,
              {range(0,18): "Should not drive",
               range(18,90): "Can drive"},
              default="Should not drive")
        >> "Can drive"

    Args:
        variable (any): The variable to be matched.
        dictionary (dict): A dictionary containing keys to be matched against
                           and results to be returned. Any hashable object that
                           implements __eq__, __contains__, or is a type can
                           be used as a key.
        default=None (any): The result to return if 'variable' cannot be
                            matched to any key in 'dictionary'.

    Returns:
        any: The matching result from 'dictionary' or 'default'.
    """

    # match(5, {5:"five"})
    if variable in dictionary:
        return dictionary[variable]

    for key, val in dictionary.items():

        # match(5, {5 > 10:"5 is greater than 10"})
        if key is True:
            return val

        # match(5, {int:"5 is an integer"})
        if type(key) is type:
            if isinstance(variable, key):
                return val
            continue

        if not hasattr(key, "__contains__"):
            continue

        # match(5, {range(0,10):"5 is between 0 and 10"})
        if isinstance(key, range):
            check = int(variable)

        # match(5, {(1,2,5):"5 is in the tuple"})
        else:
            check = variable

        if check in key:
            return val

    return default
