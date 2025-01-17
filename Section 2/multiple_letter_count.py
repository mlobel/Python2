def multiple_letter_count(phrase):
    letter_count = {}
    for letter in phrase:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    print(letter_count)
    return letter_count





"""Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

multiple_letter_count('yay')
multiple_letter_count('Yay')