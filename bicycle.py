import numpy as np
import math

"""
Allows for easy bicycle model math.
"""
class Bicycle:
    def __init__(self, wheelbase: float, radius: float) -> None:
        self.wheelbase = wheelbase
        self.radius = radius

    def calculate_steering_angle(self, turning_radius):
        return math.atan(self.wheelbase / turning_radius)
    
    def calculate_angular_velocity(self, linear_velocity, turning_radius):
        return linear_velocity / turning_radius
    
    def calculate_wheel_rotation_speed(self, linear_velocity):
        return linear_velocity / self.radius