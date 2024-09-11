def last_element(lst):
    if lst:
        last_item = len(lst) - 1
        print (lst[last_item])
        return lst[last_item]
    else:
        print("None")
        return None

    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

last_element([1, 2, 3])
last_element([]) is None