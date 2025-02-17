from differential_drive import DifferentialDrive
from bicycle import Bicycle
from planar_arm import PlanarArm
import math

TURTLE_BOT_WHEEL_DIAMETER = .07 # meters
TURTLE_BOT_WHEEL_RADIUS = TURTLE_BOT_WHEEL_DIAMETER / 2
TURTLE_BOT_WHEEL_BASE = .23 # meters
TURTLE_BOT = DifferentialDrive(TURTLE_BOT_WHEEL_RADIUS, TURTLE_BOT_WHEEL_BASE)

BICYCLE_WHEEL_DIAMETER =.7 # meters
BICYCLE_WHEEL_RADIUS = BICYCLE_WHEEL_DIAMETER / 2
BICYCLE_WHEELBASE = 0.983 # meters
BICYCLE = Bicycle(BICYCLE_WHEEL_RADIUS, BICYCLE_WHEELBASE)

PLANAR_ARM_LENGTHS = (2., 1.5)
PLANAR_ARM = PlanarArm(PLANAR_ARM_LENGTHS)

if __name__ == "__main__":
    # Problem 1
    forward_velocity = 0.4 # m/s
    turning_radius = 2.5 # m

    rotation_rate = TURTLE_BOT.calculate_angular_velocity(forward_velocity, turning_radius)
    left_wheel_velocity, right_wheel_velocity = TURTLE_BOT.calculate_wheel_velocity(forward_velocity, turning_radius)

    print(f"Turtle Bot rotation rate: {rotation_rate} rad/s")
    print(f"Turtle Bot left wheel velocity: {left_wheel_velocity} m/s")
    print(f"Turtle Bot right wheel velocity: {right_wheel_velocity} m/s")
    print()

    # Problem 2
    forward_velocity = 2.0 # m/s
    turning_radius = 6.5 # m

    steering_angle = BICYCLE.calculate_steering_angle(turning_radius)
    angular_velocity = BICYCLE.calculate_angular_velocity(forward_velocity, turning_radius)
    wheel_rotation_speed = BICYCLE.calculate_wheel_rotation_speed(forward_velocity)
    
    print(f"Bicycle steering angle: {math.degrees(steering_angle)} deg")
    print(f"Bicycle angular velocity: {angular_velocity} rad/s")
    print(f"Bicycle wheel rotation speed: {wheel_rotation_speed} rad/s")
    print()

    # Problem 3
    left_wheel_angular_velocity = 8.3 # rad/s
    right_wheel_angular_velocity = 7.7 # rad/s

    linear_velocity, angular_velocity = TURTLE_BOT.calculate_body_velocities(left_wheel_angular_velocity, right_wheel_angular_velocity)
    radius_of_curvature = TURTLE_BOT.calculate_radius_of_curvature(linear_velocity, angular_velocity)
    print(f"Turtle Bot velocity: {linear_velocity} m/s")
    print(f"Turtle Bot velocity: {angular_velocity} rad/s")
    print(f"Turtle Bot radius of curvature: {radius_of_curvature} m")
    print()

    # Problem 4
    desired_points = [ # the arm is elevated by .5 so I'm subtracting .5 from the y's
        [2., 1.5],
        [2.82, 2.82],
        [2.47, 2.47],
        [.5, .5]
    ]
    for point in desired_points:
        x, y = point
        adjusted_y = y -.5

        if PLANAR_ARM.is_reachable((x, adjusted_y)):
            angles_1, angles_2 = PLANAR_ARM.calculate_segment_angles((x, adjusted_y))
            print(f"Point {point} can be reached with {angles_1} or {angles_2}")
        else:
            print(f"Point {point} is unreachable by the arm")
    print()

    # Problem 5
    forward_velocity = .25 # m/s
    turning_radius = 3.0 # m

    rotation_rate = TURTLE_BOT.calculate_angular_velocity(forward_velocity, turning_radius)
    left_wheel_velocity, right_wheel_velocity = TURTLE_BOT.calculate_wheel_velocity(forward_velocity, turning_radius)
    straight_left_wheel_velocity, straight_right_wheel_velocity = TURTLE_BOT.calculate_wheel_velocity(forward_velocity, 0.0)

    print(f"Turtle Bot rotation rate: {rotation_rate} rad/s")
    print(f"Turtle Bot left wheel velocity: {left_wheel_velocity} m/s")
    print(f"Turtle Bot right wheel velocity: {right_wheel_velocity} m/s")
    print(f"Turtle Bot straight left wheel velocity: {straight_left_wheel_velocity} m/s")
    print(f"Turtle Bot straight right wheel velocity: {straight_right_wheel_velocity} m/s")
    print()