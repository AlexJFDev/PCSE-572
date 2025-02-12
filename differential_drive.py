import numpy as np

"""
Allows for easy differential drive math.
"""
class DifferentialDrive:
    def __init__(self, wheel_radius: float|int, wheel_base: float|int) -> None:
        self.wheel_radius = wheel_radius
        self.wheel_base = wheel_base

    def calculate_angular_velocity(self, linear_velocity: float|int, turning_radius: float|int) -> float:
        if turning_radius == 0: return 0.
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
    
    def calculate_body_velocities(self, left_wheel_velocity: float|int, right_wheel_velocity: float|int) -> tuple[float, float]:
        wheel_base_matrix = np.array([
            [ self.wheel_radius / 2, self.wheel_radius / 2 ],
            [ self.wheel_radius / self.wheel_base, -self.wheel_radius / self.wheel_base ]
        ])
        wheel_velocity_matrix = np.array([
            [ right_wheel_velocity ],
            [ left_wheel_velocity  ]
        ])
        print(wheel_base_matrix)
        print(wheel_velocity_matrix)
        body_velocity_matrix = wheel_base_matrix @ wheel_velocity_matrix

        return body_velocity_matrix[0][0], body_velocity_matrix[1][0]
    
    def calculate_radius_of_curvature(self, linear_velocity, angular_velocity) -> float|int:
        return linear_velocity / angular_velocity