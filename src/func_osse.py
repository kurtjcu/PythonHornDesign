"""
Osse via ATH formula
Credit to the original author of Oblate Sphereoid in compression drivers, ER Geddes. 

I just made a python implementation of it from below (M Batic) who has added some convenient functions including the roundover for the mouth terminations.
Mu implementation is NOT EXACTLY the same as the original, but it is (hopefully) close enough for the purpose of this project. 
https://at-horns.eu/

Desmos calc of OSSE by M Batic
https://www.desmos.com/calculator/igr6jwvi9d


"""

import numpy as np


def osse(x_point, horn_length, dispertion_angle, throat_radius, throat_angle, k=1, s=0.7, q=0.996, n=2):
    """
    Calculates the Osse value using the ATH formula.

    Parameters:
    - x_point (float): The x-coordinate, distance from the horn throat in mm.
    - horn_length - L (float): Length of the horn in mm.
    - dispertion_angle - alpha (float): Dispertion angle / 2.
    - throat_radius - r_0 (float): Radius of the horn at the throat in mm.
    - throat_angle - alpha_0 (float): Angle of the horn at the throat.
    - k (float, optional): Scaling factor for the throat radius, Expansion factor Default is 1. ( 0 < k < 10) if K= 0 it is a conical horn
    - s (float, optional): Scaling factor for the roundover, Superellipse aspect ratio. Default is 0.7.
    - q (float, optional): Scaling factor for the roundover, Superellipse termination (truncation coefficient). Default is 0.996. (0.990 < s < 1.000)
    - n (int, optional): Exponent for the roundover, superellipse exponent (compress superelipse), lower numbers = lower frequency cutoff. Default is 2. (2.0 < n < 10.0)

    Returns:
    - osse_value (float): The calculated Osse value at that position. i.e. if x_point=x then returns y

    """
    # calculate the parts of the formula
    throat_radius = np.power((k * throat_radius), 2)
    os_curve = np.power((np.tan(90 - dispertion_angle) * x_point), 2)
    throat_angle = (2 * k) * np.tan(90 - throat_angle) * x_point
    expansion = throat_radius * (1 - k)
    roundover = (
        horn_length * s / q * (1 - np.power((1 - np.power(((q * x_point) / horn_length), n)), 1 / n))
    )

    return np.sqrt(throat_radius + os_curve + throat_angle) + expansion + roundover
