# A function that accepts any number of arguments

def receptor(*args):
    """
    The receptor function accepts any type of arguments and provides a summary.
    Uses the instanceof.

    :param args: Accepts any positional arguments
    :return: A summary of the datatypes.
    """

    number_of_ints = 0
    number_of_strings = 0
    number_of_floats = 0
    number_of_bools = 0
    number_of_lists = 0
    number_of_unsupported_types = 0

    for items in args:
        if isinstance(items, int):
            number_of_ints += 1
        elif isinstance(items, str):
            number_of_strings += 1
        elif isinstance(items, float):
            number_of_floats += 1
        elif isinstance(items, bool):
            number_of_bools += 1
        elif isinstance(items, list):
            number_of_lists += 1
        else:
            number_of_unsupported_types += 1

    return {
        'number_of_ints': number_of_ints,
        'number_of_strings': number_of_strings,
        'number_of_floats': number_of_floats,
        'number_of_bools': number_of_bools,
        'number_of_lists': number_of_lists,
        'number_of_unsupported_types': number_of_unsupported_types,
    }

# test
print(receptor(1,
               2,
               3.0,
               (2,3,4,4), # unsupported
               [23,34,23],
               {
                   'GAME':'NIGHT'
               },
               "Ian", "Biran",
               False, False, True,
               "Nathan", 2,34,
               [23,"ian","34"]
               ))