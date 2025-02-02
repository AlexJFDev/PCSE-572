import math
import numpy as np

from quaternion import Quaternion

# For typing
from typing import Optional

AXIS_TABLE: dict[str, tuple[float, float, float]] = {
    "x" : (1., 0., 0.),
    "y" : (0., 1., 0.),
    "z" : (0., 0., 1.)
}

class Rotation:
    def __init__(
            self,
            axis: Optional[str|list[int|float]]=None,
            angle: Optional[int|float]=None,
            rotation_matrix: Optional[np.matrix[int|float, int|float]]=None,
            quaternion: Optional[Quaternion]=None, 
            radians: bool=True
        ) -> None:
        """
        The arguments should be in one of three forms:
            One:
                axis should be a string, "x", "y", or "z".
                angle is a number.
            Two:
                rotation_matrix is a list of lists with 3 numbers
            Three:
                quaternion is a list of 4 numbers
        angle is assumed to be in radians unless radians=False
        """
        # axis and angle
        if (axis is not None and angle is not None) and (rotation_matrix is None and quaternion is None):
            # Validate axis
            if isinstance(axis, str):
                axis = axis.lower()
                if axis in AXIS_TABLE.keys():
                    axis = AXIS_TABLE[axis]
                else:
                    raise ValueError('Axis should either be a list of 3 numbers or a string "x" "y" or "z"')
            else:
                if len(axis) != 3:
                    raise ValueError("Length of axis should be 3")
                for i, n in enumerate(axis):
                    new_axis = []
                    if isinstance(n, (int, float)):
                        new_axis.append(float(n))
                    else:
                        raise ValueError(f"{n} at index {i} of axis is of the wrong type")
                    axis = new_axis
            # Validate Angle
            if isinstance(angle, int):
                angle = float(angle)
            elif not isinstance(angle, float):
                raise ValueError(f"angle {angle} should be an int or a float")
            
            self.axis = axis
            self.angle = angle
            self.rotation_matrix = Rotation.__generate_rotation_matrix(axis, angle, radians=radians)
            self.rotation_quaternion = Rotation.__generate_rotation_quaternion(axis, angle, radians=radians)
        # Rotation matrix
        elif (rotation_matrix is not None) and (axis is None and angle is None and quaternion is None):
            raise NotImplementedError("TODO")
        # Quaternion
        elif (quaternion is not None) and (axis is None and angle is None and rotation_matrix is None):
            raise NotImplementedError("TODO")
        else:
            raise ValueError("Please provide an axis and angle, or a rotation matrix, or a quaternion. Do not provide any other combination.")

    def __generate_rotation_matrix(axis:tuple[float, float, float], angle:float, radians=True) -> np.matrix[float, float]:
        """
        Generates a rotation angle from the provided axis and angle. 
        Assumes angle is in radians unless radians=False.
        """
        if radians:
            angle_radians = angle
        else:
            angle_radians = math.radians(angle)
        x, y, z = axis

        identity_3 = np.identity(3)
        k = np.matrix([
            [0, -z, y],
            [z, 0, -x],
            [-y, x, 0]
        ])

        angle_sin = math.sin(angle_radians)
        angle_cos = math.cos(angle_radians)
        # Rodrigues' Rotation
        return identity_3 + angle_sin * k + (1 - angle_cos) * k * k
        


    def __generate_rotation_quaternion(axis:tuple[float, float, float], angle:float, radians=True) -> Quaternion:
        """
        Generates a rotation quaternion from the provided axis and angle. 
        Assumes angle is in radians unless radians=False.
        """
        if radians:
            angle_radians = angle
        else:
            angle_radians = math.radians(angle)
        x, y, z = axis

        angle_cos = math.cos(2 / angle_radians)
        angle_sin = math.cos(2 / angle_radians)

        w = angle_cos
        x_ = x * angle_sin
        y_ = y * angle_sin
        z_ = z * angle_sin

        return Quaternion(w, x_, y_, z_)
