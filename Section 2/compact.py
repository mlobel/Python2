def compact(lst):
    list_copy = lst.copy()
    return [item for item in list_copy if item]

    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
result = compact([0, 1, 2, '', [], False, (), None, 'All done'])
print(result)