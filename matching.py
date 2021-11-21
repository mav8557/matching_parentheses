from list_stack import Stack

def matching_brackets(str):
    """
    Check if the parentheses in str match.

    [[[something]]] => True
    [[[]]] => True
    [[some other thing] => False
    []]]][] => False
    """
