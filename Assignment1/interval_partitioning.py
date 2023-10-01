"""
Using Greedy Algorithm to select non-overlapping intervals. It iterates through the sorted intervals and adds
an interval to the list of partitioned intervals if it doesn't overlap with the previously selected intervals.

The reason Greedy Algorithm is suitable for this task because of it's simplicity and efficiency. This algorithm makes locally
optimal choices which will often lead to globally optimal solutions in this case (This is not guaranteed). 
The implementation is also pretty straight forward. While Greedy algorithms may work well for interval partitioning, there may also be
more complex situations where other algorithms such as dynamic programming gives better results for this type of task.

"""

from collections import namedtuple as T

Interval = T("Interval", "s f")

def partition_interval(intervals):
    """
    Partition intervals into non-overlapping partitions using a greedy algorithm.
    
    Inputs:
        intervals: list of intervals with unique start (s) and end (f) times represented as lists.

    Output:
        Returns a tuple containing the count of selected non-overlapping intervals and the intervals themselves.
    """
    # Convert lists to namedtuples
    namedtuple_intervals = [Interval(*interval) for interval in intervals]

    # Sort named intervals based on end times
    sorted_intervals = sorted(namedtuple_intervals, key=lambda x: x.f)
    visited_intervals = []
    count = 0
    end_of_interval = 0

    # Adds all non-overlapping intervals to visited_intervals
    for interval in sorted_intervals:
        if end_of_interval <= interval.s:
            end_of_interval = interval.f
            visited_intervals.append(interval)
            count += 1
    
    # Returns the maximum number of non-overlapping intervals and the count
    return count, visited_intervals

# Testing the function using random intervals
intervals = [[1, 3], [7, 12], [2, 5], [6, 18], [14, 16]]
result = partition_interval(intervals)
print(result)