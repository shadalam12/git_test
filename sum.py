def sum_of_intervals(intervals):
    ''''return the differences of array of array'''
    output = set([])
    for interval in intervals:
        if interval[0] < interval[1]:
            output.update(range(interval[0], interval[1]))
        else:
            raise KeyError('First Number Is Greater Than The Second')
    return len(output)