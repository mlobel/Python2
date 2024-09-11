def is_palindrome(phrase):
    phrase = phrase.replace(' ','')
    reversed_phrase = ''.join(reversed(phrase))
    if reversed_phrase.lower() == phrase.lower() :
        print(True)
        return True
    else:
        print(False)
        return False
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

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
is_palindrome('tacocat')
is_palindrome('noon')
is_palindrome('robert')
is_palindrome('taco cat')
is_palindrome('Noon')
