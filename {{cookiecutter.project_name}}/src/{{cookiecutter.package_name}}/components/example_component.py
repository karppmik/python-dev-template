"""Example component with a generic mathematical function."""

import math


def calculate_exponential_decay(value: float) -> float:
    """Calculate the exponential decay of a given value.

    Args:
        value (float): The input value.

    Returns:
        float: The result of applying the exponential decay formula (e^(-x)).

    Raises:
        ValueError: If the input value is negative.
    """
    if value < 0:
        raise ValueError("Input value must be non-negative.")
    
    return math.exp(-value)