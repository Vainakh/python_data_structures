def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """


    weekDays = {"Monday": 1, "Tuesday": 2, "Wednesday": 3,
            "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
    for day in weekDays.values():
        if(day == day_of_week):
            return day
    

print("weekday_name:", weekday_name(1))
print("weekday_name:", weekday_name(7))
print("weekday_name:", weekday_name(9))
print("weekday_name:", weekday_name(0))
