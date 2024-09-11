def weekday_name(day_of_week):
    days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    if 1 <= day_of_week <= 7 :
        day_name = days[day_of_week - 1]
        print(day_name)
        return day_name
    
    else:
        print("None")
        return "None"

    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """

weekday_name(1)
weekday_name(7)
weekday_name(9)
weekday_name(0)