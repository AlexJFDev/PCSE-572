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
    axis: float
    angle: float
    rotation_matrix: np.ndarray[float]
    rotation_quaternion: Quaternion

    def __init__(
            self,
            axis: Optional[str|list[int|float]]=None,
            angle: Optional[int|float]=None,
            rotation_matrix: Optional[np.ndarray[int|float, int|float]]=None,
            rotation_quaternion: Optional[Quaternion]=None, 
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
        if not isinstance(radians, bool):
            raise ValueError(f"radians should be a boolean")
        # axis and angle
        if (axis is not None and angle is not None) and (rotation_matrix is None and rotation_quaternion is None):
            # Validate axis
            self.angle = Rotation.__validate_angle(angle)
            self.axis = Rotation.__validate_axis(axis)
            self.rotation_matrix = Rotation.__axis_angle_to_rotation_matrix(self.axis, self.angle, radians=radians)
            self.rotation_quaternion = Rotation.__axis_angle_to_rotation_quaternion(self.axis, self.angle, radians=radians)
        # Rotation matrix
        elif (rotation_matrix is not None) and (axis is None and angle is None and rotation_quaternion is None):
            self.rotation_matrix = Rotation.__validate_rotation_matrix(rotation_matrix)
            raise NotImplementedError("TODO")
        # Quaternion
        elif (rotation_quaternion is not None) and (axis is None and angle is None and rotation_matrix is None):
            self.rotation_quaternion = Rotation.__validate_rotation_quaternion(rotation_quaternion)

            self.axis, self.angle = Rotation.__rotation_quaternion_to_axis_angle(self.rotation_quaternion)
            self.rotation_matrix = Rotation.__rotation_quaternion_to_rotation_matrix(self.axis, self.angle, radians=radians)
            raise NotImplementedError("TODO")
        else:
            raise ValueError("Please provide an axis and angle, or a rotation matrix, or a quaternion. Do not provide any other combination.")
        
    def __validate_axis(axis: str|list[int|float]):
        if isinstance(axis, str):
            new_axis = axis.lower()
            if new_axis in AXIS_TABLE.keys():
                new_axis = AXIS_TABLE[new_axis]
            else:
                raise ValueError('Axis should either be a list of 3 numbers or a string "x" "y" or "z"')
        else:
            if len(axis) != 3:
                raise ValueError("Length of axis should be 3")
            for i, n in enumerate(axis):
                if not isinstance(n, (int, float)):
                    raise ValueError(f"{n} at index {i} of axis is of the wrong type")
            new_axis = (float(axis[0]), float(axis[1]), float(axis[2]))
        return new_axis
    
    def __validate_angle(angle: int|float):
        if not isinstance(angle, (int, float)):
            raise ValueError(f"angle {angle} should be an int or a float")
        return float(angle)
    
    def __validate_rotation_matrix(
            rotation_matrix: 
                np.ndarray[int|float, int|float] | 
                list[list|tuple[int|float]] | 
                tuple[list|tuple[int|float]]
        ):
        if isinstance(rotation_matrix, (list, tuple)):
            if len(rotation_matrix) != 3:
                raise ValueError("rotation_matrix should of length 3")
            for i, row in enumerate(rotation_matrix):
                if len(row) != 3:
                    raise ValueError(f"row {i} of rotation_matrix should be of length 3")
                for j, n in enumerate(row):
                    if not isinstance(n, (int, float)):
                        raise ValueError(f"{n} at index {j} of row {i} of rotation_matrix is of the wrong type")
        elif isinstance(rotation_matrix, np.ndarray):
            if rotation_matrix.shape != (3, 3):
                raise ValueError("rotation_matrix should be of shape (3, 3)")
            if np.issubdtype(rotation_matrix.dtype, np.integer) or np.issubdtype(rotation_matrix.dtype, np.floating):
                raise ValueError("rotation_matrix should be of floating point or integer numbers")
        else:
            raise ValueError("rotation_matrix should be a list or tuple or a numpy array")
        return np.array(rotation_matrix, dtype=float)
    
    def __validate_rotation_quaternion(
            rotation_quaternion: 
                Quaternion |
                list[int|float] |
                tuple[int|float]
            ):
        if isinstance(rotation_quaternion, Quaternion):
            return rotation_quaternion.copy()
        elif isinstance(rotation_quaternion, (list, tuple)):
            if len(rotation_quaternion) != 4:
                raise ValueError("rotation_quaternion should of length 4")
            for i, n in enumerate(rotation_quaternion):
                if not isinstance(n, (int, float)):
                    raise ValueError(f"{n} at index {i} of rotation_quaternion is of the wrong type")
        else:
            raise ValueError("rotation_quaternion should be a Quaternion or a list or tuple")
        return Quaternion(*rotation_quaternion)

    def __axis_angle_to_rotation_matrix(axis:tuple[float, float, float], angle:float, radians=True) -> np.ndarray[float, float]:
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
        k = np.asarray([
            [  0., -z,   y  ],
            [  z,   0., -x  ],
            [ -y,   x,   0. ]
        ])

        angle_sin = math.sin(angle_radians)
        angle_cos = math.cos(angle_radians)
        # Rodrigues' Rotation
        return identity_3 + angle_sin * k + (1 - angle_cos) * k @ k

    def __axis_angle_to_rotation_quaternion(axis:tuple[float, float, float], angle:float, radians=True) -> Quaternion:
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

    def __rotation_quaternion_to_rotation_matrix(rotation_quaternion: Quaternion) -> np.ndarray[float, float]:
        w, x, y, z = rotation_quaternion.component_array
        return np.array([
            [ 1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)],
            [ 2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)],
            [ 2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)]
        ])
    
    def __rotation_quaternion_to_axis_angle(rotation_quaternion: Quaternion) -> tuple[tuple[float, float, float], float]:
        w, x_q, y_q, z_q = rotation_quaternion.component_array
        angle = 2 * math.acos(w)
        
        angle_sin = math.sin(angle / 2)

        if math.isclose(angle_sin, 0):
            axis = (1, 0, 0)
        else:
            axis = (x_q / angle_sin, y_q / angle_sin, z_q / angle_sin)

        return axis, angle