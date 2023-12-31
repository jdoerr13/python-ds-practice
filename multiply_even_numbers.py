def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    evenNums = [n for n in nums if n % 2 == 0]
    product = 1 if not evenNums else evenNums[0]
    for num in evenNums[1:]:
        product *= num
    return product