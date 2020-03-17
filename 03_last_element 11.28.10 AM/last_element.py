def last_element(lst):
    """Return last item in list (None if list is empty.)
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if (len(lst) == 0):
        return True
    else:
        return lst.pop()

print("last_element", last_element([1, 2, 3]))#3  
print("last_element", last_element([1, 4, 3, 23, 12]))  #12
print("last_element", last_element([10, 20, 30, 40, 50]))  #50
print("last_element", last_element([])) #None
