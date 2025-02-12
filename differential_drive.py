import numpy as np

"""
Allows for easy differential drive math.
"""
class DifferentialDrive:
    def __init__(self, wheel_radius: float|int, wheel_base: float|int) -> None:
        self.wheel_radius = wheel_radius
        self.wheel_base = wheel_base

    def calculate_angular_velocity(self, linear_velocity: float|int, turning_radius: float|int) -> float|int:
        return linear_velocity / turning_radius
    
    def calculate_wheel_velocity(self, linear_velocity: float|int, turning_radius: float|int) -> float|int:
        angular_velocity = self.calculate_angular_velocity(linear_velocity, turning_radius)

        wheel_base_matrix = np.array([
            [ 1, -self.wheel_base / 2 ],
            [ 1, self.wheel_base / 2  ]
        ])
        velocity_matrix = np.array([
            [ linear_velocity ],
            [ angular_velocity ]
        ])
        wheel_velocity_matrix = wheel_base_matrix @ velocity_matrix

        return wheel_velocity_matrix[0][0], wheel_velocity_matrix[1][0]