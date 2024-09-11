def single_letter_count(word, letter):
    new_letter = letter.upper()
    new_word = word.upper()
    count = new_word.count(new_letter)
    print(count)
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
single_letter_count("Hello World", 'h')
single_letter_count("Hello World", 'z')
single_letter_count("Hello World", 'l')