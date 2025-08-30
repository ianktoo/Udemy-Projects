# Let's play with age
# You cannot be negative age
# To calculate the year you were born, we take the current year minus your age
# You cannot be over 150 years / human max lifespan

def tell_me(name = "John Doe", age = 18):
    return name, age

print(tell_me(), type(tell_me()))


scores = [34,34,332,23,4334,564]
score = 2

def sum_list(the_list):
    '''

    Finds the sum of a list of numbers.

    :param the_list: List of numbers
    :return: sum of the_list

    :exception TypeError: if the_list is not a list

    :example: sum_list([1,2,3,4,5])
    '''

    if not isinstance(the_list, list):
        # raise an exception
        raise TypeError('Expecting a list here.')
    the_sum = 0

    for n in the_list:
        # find the sum
        the_sum = the_sum + n

    # return the result
    return the_sum

print(f'Sum of {scores} is: {sum_list(scores)}')