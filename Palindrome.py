words = ['python', 'racecar']

def reverse_string(the_string):
    '''
    Let's reverse the string.

    :exception TypeError
    :param the_string:
    :return: Reversed string
    '''

    if not isinstance(the_string, str):
        raise TypeError('Expecting a string here.')
    return the_string[::-1]

def check_palindrome(the_string):
    '''
    Accept string and check if it is a palindrome using the
    reverse_string function.

    :exception TypeError:
    :param the_string:
    :return: True if it is a palindrome, False otherwise
    '''
    if not isinstance(the_string, str):
        raise TypeError('Expecting a list here.')

    if the_string == reverse_string(the_string):
        return True
    else:
        return False

def check_palindrome_list(some_list):
    '''
    This function checks if the given list is palindrome or not.
    :param some_list:
    :return: Returns a Dictionary
    :exception TypeError:
    '''

    # We are expecting a list
    if not isinstance(some_list, list):
        raise TypeError('Expecting a list here.')

    # Define an empty dictionary
    new_dictionary = dict()

    for item in some_list:
        # Check for type errors
        if not isinstance(item, str):
            # ensure the values in the list are Stings
            raise TypeError('Expecting a string here.')

        # update the dictionary
        new_dictionary.update({item: check_palindrome(item)})

    return new_dictionary

print(check_palindrome_list(words))


# Testing - list
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_strings = ['python', 'racecar', 'pineapple', 'opo', 'ianai', 'abeba']

# print(check_palindrome_list(list_of_numbers))
print(check_palindrome_list(list_of_strings))