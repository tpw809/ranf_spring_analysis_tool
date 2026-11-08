"""Defines rot_z function."""
import numpy as np


def rot_z(g: float) -> np.ndarray:
    """Rotation matrix representing rotation about z axis.
    
    Args:
        g (float): Angle of rotation about z axis. 

    Returns:
        np.ndarray: Rotation matrix.
    """
	return np.array([
        [np.cos(g), -np.sin(g)], 
        [np.sin(g), np.cos(g)],
    ])
