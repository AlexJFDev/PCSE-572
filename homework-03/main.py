from math import pi
import math

from rotation import Rotation

ANGLES = [pi / 2, pi / 3, pi / 4, pi / 6, -pi / 3, -pi / 6]
AXES = ["x", "y", "z"]

if __name__ == "__main__":
    for angle in ANGLES:
        print(f"Angle: {angle}")
        for axis in AXES:
            print(f"\tAxis: {axis}")
            rotation = Rotation(axis=axis, angle=angle)
            print("\t\tRotation Matrix:")
            r_str = str(rotation.rotation_matrix.round(decimals=2)).replace("\n", "\n\t\t\t")
            print(f"\t\t\t{r_str}")
            print("\t\tRotation Quaternion")
            print(f"\t\t\t{rotation.rotation_quaternion.component_array.round(decimals=2)}")
        print()
