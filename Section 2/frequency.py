def frequency(lst, search_term):
    term_freq = lst.count(search_term)
    print(term_freq)
    return term_freq
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
frequency([1, 4, 3, 4, 4], 4)
frequency([1, 4, 3], 7)