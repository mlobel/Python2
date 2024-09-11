def mode(nums):
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    most_common_num = None
    highest_count = 0
    for num, count in num_counts.items():
        if count > highest_count:
            highest_count = count
            most_common_num = num
    
    print(most_common_num)
    return most_common_num


    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
mode([1, 2, 1])
mode([2, 2, 3, 3, 2])