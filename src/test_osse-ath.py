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
import plotly.graph_objects as go

L = 160  # Length of the horn
alpha = 30.0  # Dispersion angle / 2
r_0 = 12.7  # Throat radius
alpha_0 = 8  # Throat angle
k = 1.0  # Expansion factor ( 0 - 10)
s = 0.7  # Superellipse aspect ratio
q = 0.996  # Superellipse termination (truncation coefficient) 0.990 - 1.000
n = 4.0  # superellipse exponent (compress superelipse) 2.0 - 10.0, lower numbers = lower frequency cutoff

osse_coords = []  # OSSE coordinates
line_coords = []  # Dispertion line coordinates

for x in range(0, L + 1):
    # calculate the parts of the formula
    throat_radius = np.power((k * r_0), 2)
    os_curve = np.power((np.tan(90 - alpha) * x), 2)
    throat_angle = (2 * k) * np.tan(90 - alpha_0) * x
    expansion = r_0 *(1-k)
    roundover = L * s / q * (1 - np.power((1 - np.power(((q * x) / L), n)), 1 / n))

    # Complete formula calculations
    # y = np.sqrt(throat_radius + os_curve + throat_angle) + roundover
    y = np.sqrt(throat_radius + os_curve + throat_angle) + expansion + roundover

    # save the points
    osse_coords.append((x, y))
    line_coords.append((x, np.tan(90 - alpha) * x))


print(osse_coords)

# Plot the OSSE
fig = go.Figure(
    data=go.Scatter(
        name="OSSE",
        x=[coord[0] for coord in osse_coords],
        y=[coord[1] for coord in osse_coords],
        mode="lines+markers",
    )
)

# plot the dispersion line
fig.add_scatter(
    name=f"Dispertion {alpha} Deg",
    x=[coord[0] for coord in line_coords],
    y=[coord[1] for coord in line_coords],
    mode="lines+markers",
)

fig.update_layout(
    scene=dict(
        xaxis=dict(
            nticks=4,
            range=[0, 200],
        ),
        yaxis=dict(
            nticks=4,
            range=[0, 200],
        ),
    ),
    xaxis_title="X mm",
    yaxis_title="Y mm",
    # width=700,
    # margin=dict(r=20, l=10, b=10, t=10),
)

fig.update_layout(scene_aspectmode="data")
fig.update_yaxes(
    scaleanchor="x",
    scaleratio=1,
)


# Show the plot
fig.show()
