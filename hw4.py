from differential_drive import DifferentialDrive

TURTLE_BOT_WHEEL_DIAMETER = .07 # meters
TURTLE_BOT_WHEEL_BASE = .23 # meters

if __name__ == "__main__":
    turtle_bot = DifferentialDrive(TURTLE_BOT_WHEEL_DIAMETER / 2, TURTLE_BOT_WHEEL_BASE)

    forward_velocity = 0.4 # m/s
    turning_radius = 2.5 # m

    rotation_rate = turtle_bot.calculate_angular_velocity(forward_velocity, turning_radius)
    left_wheel_velocity, right_wheel_velocity = turtle_bot.calculate_wheel_velocity(forward_velocity, turning_radius)

    print(f"Turtle Bot rotation rate: {rotation_rate} rad/s")
    print(f"Turtle Bot left wheel velocity: {left_wheel_velocity} m/s")
    print(f"Turtle Bot right wheel velocity: {right_wheel_velocity} m/s")