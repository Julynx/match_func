"""
@file     match_func.py
@brief    Pattern matching as a function.
@date     21/07/2023
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
    # Exact match
    if variable in dictionary:
        return dictionary[variable]

    # Type match
    if type(variable) in dictionary:
        return dictionary[type(variable)]

    # Condition match
    if True in dictionary:
        return dictionary[True]

    for key, val in dictionary.items():

        if not hasattr(key, "__contains__"):
            continue

        if isinstance(key, range):
            check = int(variable)
        else:
            check = variable

        # Container match
        if check in key:
            return val

    return default
