def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a==b:
         return (f'Numbers are equal')
        elif a>b:
           return (f'First is greater')
        else:
          return (f'Second is greater')
    else: 
       return (f'Please enter a numbers')