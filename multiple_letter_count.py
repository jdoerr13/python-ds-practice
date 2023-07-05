def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counts = {}
    for char in phrase:
        counts[char] = counts.get(char, 0) + 1 #dictionary method that allows you to retrieve the value associated with a given key. it takes the key(char) as an argument and looks for a corresponding entry in the dictionary. If the key is found, the get() method returns the value associated with that key. If the key is not found, the get() method returns the default 0
    return counts