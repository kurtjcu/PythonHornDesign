import numpy as np
import argparse
import yaml
import plotly.graph_objects as go

from func_osse import osse
from coordinate_utils import cartesian_2_polar, rotate_2d_2_3d, polar_2_cartesian

def main(args):

    print(args)
    with open(args.definition, "r") as stream:
        try:
            horn_definition = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    print(f"horn definition file contains: \n {horn_definition}")

    # make a list of x co-ordinates
    sample_points = np.linspace(
        0,
        horn_definition["horn"]["horn_length"],
        horn_definition["horn"]["horn_length"] * horn_definition["plotting"]["samples_per_mm"],
    )
    # calculate the y co-ordinates for each of the x using horn definition
    points_cart_2d = np.array(
        list(map(lambda x: (x, osse(x, **horn_definition["horn"])), sample_points))
    )
    print(f"2d cartesian {points_cart_2d}")

    # convert the points to polar co-ordinates for easier rotation around an axis
    vector_polar_2d = np.array(list(map(cartesian_2_polar, points_cart_2d)))

    # do the rotation
    vector_polar_3d = np.array(
        list(map(lambda v: rotate_2d_2_3d(v, horn_definition["plotting"]["points_of_rotation"]), vector_polar_2d))
    )

    # convert back to cartesian to plot
    vector_cart_3d = np.array(
        list(map(lambda v: list(map(polar_2_cartesian, v)), vector_polar_3d))
    )
    # flatten to (n, 3) for easier plotting
    vector_cart_3d_flat = vector_cart_3d.reshape(-1, 3)
    # print(f"3d cartesian shape {vector_cart_3d.shape}")

    # plot the 3d points
    if horn_definition["plotting"]["generate_plot"]:
        fig = go.Figure(
            data=[
                go.Scatter3d(
                    x=vector_cart_3d_flat[:, 0],
                    y=vector_cart_3d_flat[:, 1],
                    z=vector_cart_3d_flat[:, 2],
                    mode="markers",
                )
            ]
        )
        fig.update_layout(scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="z"))
        fig.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Loads a definition of a horn profile from a yaml file and calculates an axis symetric osse waveguide."
    )
    parser.add_argument(
        "--definition",
        type=str,
        default="de250_90deg_160mm.yaml",
        help="The path to the yaml file containing the horn profile definition.",
    )
    args = parser.parse_args()
    main(args)
