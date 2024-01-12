def sum_intervals(intervals):
    unique_points = set()

    for start, end in intervals:
        unique_points.update(range(start, end))

    return len(unique_points)