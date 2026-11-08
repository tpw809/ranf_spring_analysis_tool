"""Defines involute_function."""
import numpy as np


def involute_function(phi: float) -> float:
    """Involute function."""
    theta = np.tan(phi) - phi
    return theta
