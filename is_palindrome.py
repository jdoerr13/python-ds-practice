def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> def is_palindrome(phrase):
        True

        >>> is_palindrome('Noon')
        True
    """
    reversed_string = phrase[::-1]
    if reversed_string.lower() == phrase.lower():
        return True
    return False