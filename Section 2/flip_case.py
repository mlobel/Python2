def flip_case(phrase, to_swap):
    to_swap_lower = to_swap.lower()
    to_swap_upper = to_swap.upper()
    swap_phrase = ''

    for letter in phrase:
        if letter == to_swap_lower:
            swap_phrase += to_swap_upper
        elif letter == to_swap_upper:
            swap_phrase += to_swap_lower
        else:
            swap_phrase += letter

    print(swap_phrase)
    return swap_phrase
        
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

flip_case('Aaaahhh', 'a')
flip_case('Aaaahhh', 'A')
flip_case('Aaaahhh', 'h')