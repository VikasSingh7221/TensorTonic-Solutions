import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    total_distance = 0
    for i in range(len(x)):
        total_distance += abs(y[i] - x[i])

    return float(total_distance)
        