import math

class Rotation:
    def __init__(self, axis=None, angle=None, rotation_matrix=None, quaternion=None, radians=True):
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

        if axis in {"x", "y", "z"} and angle is not None:
            self.axis = axis
            self.angle = angle
            self.rotation_matrix = Rotation.generate_rotation_matrix(axis, angle, raidians=False)
        elif rotation_matrix is not None:
            self.rotation_matrix = rotation_matrix
        elif quaternion is not None:
            self.quaternion = quaternion
        else:
            raise ValueError

    def generate_rotation_matrix(axis, angle, radians=True):
        """
        Generates a rotation angle from the provided axis and angle. 
        Assumes angle is in radians unless radians=False.
        """
        if radians:
            angle_radians = angle
        else:
            angle_radians = math.radians(angle)
        
        angle_cos = math.cos(angle_radians)
        angle_sin = math.cos(angle_radians)

        if axis == "x":
            return [
                [ 1,         0,          0 ],
                [ 0, angle_cos, -angle_sin ], 
                [ 0, angle_sin, angle_cos  ]
            ]
        elif axis == "y":
            return [
                [ angle_cos,  0, angle_sin ],
                [ 0,          1,         0 ], 
                [ -angle_sin, 0, angle_cos ]
            ]
        elif axis == "z":
            return [
                [ angle_cos, -angle_sin, 0 ],
                [ angle_sin, angle_cos,  0 ], 
                [ 0,         0,          1 ]
            ]
        else:
            raise ValueError