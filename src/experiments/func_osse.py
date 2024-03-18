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


def osse(x_point, L, alpha, r_0, alpha_0, k=1, s=0.7, q=0.996, n=2):
    """
    Calculates the Osse value using the ATH formula.

    Parameters:
    - x_point (float): The x-coordinate, distance from the horn throat in mm.
    - L (float): Length of the horn in mm.
    - alpha (float): Dispertion angle / 2.
    - r_0 (float): Radius of the horn at the throat in mm.
    - alpha_0 (float): Angle of the horn at the throat.
    - k (float, optional): Scaling factor for the throat radius, Expansion factor Default is 1. ( 0 < k < 10)
    - s (float, optional): Scaling factor for the roundover, Superellipse aspect ratio. Default is 0.7.
    - q (float, optional): Scaling factor for the roundover, Superellipse termination (truncation coefficient). Default is 0.996. (0.990 < s < 1.000)
    - n (int, optional): Exponent for the roundover, superellipse exponent (compress superelipse), lower numbers = lower frequency cutoff. Default is 2. (2.0 < n < 10.0)

    Returns:
    - osse_value (float): The calculated Osse value at that position. i.e. if x_point=x then returns y

    """
    # calculate the parts of the formula
    throat_radius = np.power((k * r_0), 2)
    os_curve = np.power((np.tan(90 - alpha) * x_point), 2)
    throat_angle = (2 * k) * np.tan(90 - alpha_0) * x_point
    expansion = r_0 * (1 - k)
    roundover = (
        L * s / q * (1 - np.power((1 - np.power(((q * x_point) / L), n)), 1 / n))
    )

    return np.sqrt(throat_radius + os_curve + throat_angle) + expansion + roundover
