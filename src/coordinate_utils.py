import numpy as np

def cartesian_2_polar(cart_xy):
    """Converts cartesian co-ordinates to polar co-ordinates. returns (rho, phi) where phi is in radians."""
    x, y = cart_xy
    rho = np.hypot(x, y)
    theta = np.arctan2(y, x)
    return (rho, theta)


def rotate_2d_2_3d(polar_2d, points_of_rotation):
    """Rotates a 2d vector around the z axis by the number of points of rotation."""
    degrees_of_rotation = np.linspace(0, 360, points_of_rotation)
    r, theta = polar_2d
    return np.array([[r, theta, np.radians(degree)] for degree in degrees_of_rotation])


def polar_2_cartesian(polar_3d):
    """Converts polar co-ordinates to cartesian co-ordinates. returns (x, y, z)"""
    r, theta, phi = polar_3d
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return (x, y, z)