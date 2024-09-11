def vowel_count(phrase):
    vowels = 'aeiou'
    phrase = phrase.lower()
    return {vowel: phrase.count(vowel) for vowel in vowels if vowel in phrase}
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    
print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))