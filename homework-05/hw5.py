from transform import Transformation
from rotation import Rotation
import math
import numpy as np

robot_rotation = Rotation(axis="z", angle=math.pi / 4)
robot_transform = Transformation((-2.75, -.75, 0), robot_rotation)
print(robot_transform.transformation_matrix)

robot_location = np.array([
    [-2.75],
    [-.75],
    [0]
])
world_intersection = np.array([
    [-1.93421],
    [0.50876],
    [0],
    [1]
])

#world_robot_difference = world_intersection - robot_location

#print(world_robot_difference)
#print(robot_rotation.rotation_matrix @ world_robot_difference)
inverse = np.linalg.inv(robot_transform.transformation_matrix)
print(inverse @ world_intersection)