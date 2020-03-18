def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    newPhrase = ''
    for letter in phrase:
        if letter == to_swap:
            letter = letter.swapcase()
            newPhrase += letter
        else:
            newPhrase += letter
    return newPhrase


print("flipped right if aAAAhhh:", flip_case("Aaaahhh", "a"))  
print("flipped right if aAAAhhh:", flip_case("Aaaahhh", "A")) 
print("flipped right if AaaaHHH:", flip_case("Aaaahhh", "h"))
