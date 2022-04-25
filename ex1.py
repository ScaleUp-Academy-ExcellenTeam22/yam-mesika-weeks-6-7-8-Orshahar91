from collections import defaultdict


def group_by(function, iterable):
    #  this function groups values by the returned value
    #  from the function that is provided and returns the dictionary
    dictionary = defaultdict(list)  # creates an empty dictionary with empty list as value

    key_and_value_tuple = []  # list of tuples

    for value in iterable:
        key_and_value_tuple.append((function(value), value))

    for key, value in key_and_value_tuple:
        dictionary[key].append(value)

    return dictionary
