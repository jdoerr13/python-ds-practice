def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
#    (non-zero, non-empty, non-False)
    return [x for x in lst if x]

    # result = []
    # for x in lst:
    #     if x:
    #         result.append(x)
    # return result
