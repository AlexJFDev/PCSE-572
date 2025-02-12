from differential_drive import DifferentialDrive
from bicycle import Bicycle
import math

TURTLE_BOT_WHEEL_DIAMETER = .07 # meters
TURTLE_BOT_WHEEL_BASE = .23 # meters

BICYCLE_WHEELBASE = 0.983 # meters
BICYCLE_WHEEL_DIAMETER =.7 # meters

if __name__ == "__main__":
    turtle_bot = DifferentialDrive(TURTLE_BOT_WHEEL_DIAMETER / 2, TURTLE_BOT_WHEEL_BASE)
    # Problem 1
    forward_velocity = 0.4 # m/s
    turning_radius = 2.5 # m

    rotation_rate = turtle_bot.calculate_angular_velocity(forward_velocity, turning_radius)
    left_wheel_velocity, right_wheel_velocity = turtle_bot.calculate_wheel_velocity(forward_velocity, turning_radius)

    print(f"Turtle Bot rotation rate: {rotation_rate} rad/s")
    print(f"Turtle Bot left wheel velocity: {left_wheel_velocity} m/s")
    print(f"Turtle Bot right wheel velocity: {right_wheel_velocity} m/s")
    print()

    # Problem 2
    bicycle = Bicycle(BICYCLE_WHEEL_DIAMETER / 2, BICYCLE_WHEELBASE)
    forward_velocity = 2.0 # m/s
    turning_radius = 6.5 # m

    steering_angle = bicycle.calculate_steering_angle(turning_radius)
    angular_velocity = bicycle.calculate_angular_velocity(forward_velocity, turning_radius)
    wheel_rotation_speed = bicycle.calculate_wheel_rotation_speed(forward_velocity)
    
    print(f"Bicycle steering angle: {math.degrees(steering_angle)} deg")
    print(f"Bicycle angular velocity: {angular_velocity} rad/s")
    print(f"Bicycle wheel rotation speed: {wheel_rotation_speed} rad/s")
    print()