def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversedPhrase = phrase[::-1]
    return reversedPhrase

print("reverse_string", reverse_string("awesome"))
print("reverse_string", reverse_string("sauce"))
