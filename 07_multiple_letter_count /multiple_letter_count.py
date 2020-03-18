def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict = {}

    for letter in phrase:
        dict[letter] = dict.get(letter, 0) + 1
    return dict

print("multiple_letter_count:", multiple_letter_count("yay"))#{'y': 2, 'a': 1}
print("multiple_letter_count:", multiple_letter_count("Yay"))#{'Y': 1, 'a': 1, 'y': 1}
print("multiple_letter_count:", multiple_letter_count("Naya"))#{'N': 1, 'a': 2, 'y': 1}
