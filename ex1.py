from collections import defaultdict
from collections.abc import Iterable, Callable


def group_by(function: Callable, iterable: Iterable) -> dict[object, list]:
    """
    This function groups values by the returned value from the function that is provided and returns the dictionary.
    :param function: The function to run on the iterable.
    :param iterable: The iterable to be run by the function provided.
    :return: Dictionary of grouped by value.
    """

    key_and_value_tuple = [(function(value), value) for value in iterable]

    dictionary = {key: value for (key, value) in key_and_value_tuple}

    return dictionary


"Driver code to test the function above."
print(group_by(len, ["hi", "bye", "yo", "try"]))
