import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.transforms as transforms

# Set NumPy print options to display numbers with 3 decimal places
np.set_printoptions(precision=3, floatmode='fixed')

# Constants
robot_diameter = 0.24  # meters
robot_wheelbase = 0.23  # meters
robot_wheel_diameter = 0.070  # meters

trailer_length = 0.60   # meters
trailer_diameter = 0.4  # meters


# Calculate linear speed based on circular motion (v = omega * r)
# Assuming a complete circle is covered in x seconds
time_to_complete_circle = 20 # 30  # seconds
arc_radius = 3.0      # meters

# Initialize positions and angles
robot_x, robot_y = arc_radius, 0  # Starting at (r, 0)
robot_theta = np.pi / 2  # facing upwards
trailer_phi = np.pi / 2  # Initial angle of the trailer w.r.t robot

# Calculate the required constant velocities
wz = 2 * np.pi / time_to_complete_circle  # rad/s
vb = wz * arc_radius            # m/s

# Time parameters
dt = 0.033  # time step for animation and integration (33 ms = 30 fps)
total_time = time_to_complete_circle  # total animation time
print(f"total time  = {total_time}")
print(f"vb={vb:.3f} m/s")
print(f"wz={wz:.3f} radians/s")
steps = int(total_time/dt) + 1
print("total steps = ", steps)

# Lists to store positions for animation
robot_state = np.zeros((4, steps))
trailer_positions = np.zeros((2, steps))

# Initial conditions
step = 0
robot_state[0, step] = robot_x
robot_state[1, step] = robot_y
robot_state[2, step] = robot_theta
robot_state[3, step] = trailer_phi

trailer_positions[0, step] = robot_state[0, step] - (trailer_length * np.cos(robot_theta + trailer_phi))
trailer_positions[1, step] = robot_state[1, step] - (trailer_length * np.sin(robot_theta + trailer_phi))

# Simulation loop
time = np.arange(0.0, total_time + dt/2, dt)

for t in time[1:]: # np.arange(dt, total_time, dt):
    # Update robot position and orientation
    step += 1
    # Copy prior state forward for integration
    robot_state[:, step] = robot_state[:, step-1]
    #time += dt

    # Do integration at a finer step than visualization
    # to improve accuracty
    dts = dt/10  # small time step
    for _ in range(10):  # small step integration
        theta = robot_state[2, step]
        phi = robot_state[3, step]
        # affine vector fields
        g1 = np.array([np.cos(theta), np.sin(theta), 0, np.sin(-phi)/trailer_length]).T
        g2 = np.array([0, 0, 1, -1]).T

        # State velocity calcuation (dX/dt)
        dX = g1*vb + g2*wz
        # print(dX.T)
        # Simple Euler integration X[k] = X[k-1] + dX/dt * dt
        robot_state[:, step] = robot_state[:, step] + dX*dts

    # Calculate trailer position
    theta = robot_state[2, step]
    phi = robot_state[3, step]
    trailer_positions[0, step] = robot_state[0, step] - (trailer_length * np.cos(theta + phi))
    trailer_positions[1, step] = robot_state[1, step] - (trailer_length * np.sin(theta + phi))

    # Calculate the trailer velocity in world frame
    # vx = dx / dt, vy = dy/dt
    vtw = np.diff(trailer_positions[:, (step-1):step+1])/dt  # approximate velocity of trailer in world frame
    # print(f"vtw={vtw.T} {np.dot(vtw.T, vtw)[0][0]} {vb}")
    ang = theta + phi # Angle of trailer w.r.t. the world x-axis
    Rbw = np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])
    vtb = np.dot(Rbw, vtw) # rotate to body frame

    # body dy/dt should be close to zero (but some numerical inaccuracy expected)
    print(f"{step:3d} vtw={vtw.T[0]} vtb={vtb.T[0]} speed={np.sqrt(np.dot(vtw.T, vtw)[0][0]):.3f} {np.sqrt(np.dot(vtb.T, vtb)[0][0]):.3f} {vb:.3f}")

# Animation
fig = plt.figure()
plt.plot(time, robot_state[3, :]*180/np.pi, 'r', linewidth=2)
plt.title("Trailer Angle")
plt.xlabel('time (seconds)')
plt.ylabel('phi (degrees)')
plt.grid()

fig, ax = plt.subplots()

def plot_system(robot_posn, trailer_posn):
    robot_x, robot_y, theta, phi = robot_posn
    trailer_x, trailer_y = trailer_posn

    # Draw the robot body
    body_circle = plt.Circle((robot_x, robot_y), robot_diameter / 2, color='blue', fill=False)
    ax.add_artist(body_circle)

    # Calculate wheel positions and dimensions
    wheel_height = robot_wheel_diameter
    wheel_width = robot_wheelbase / 10  # or any other appropriate value for the wheel thickness
    c_offset = robot_wheelbase / 2 + wheel_height / 2
    wheel_x_offset = c_offset * np.cos(theta)
    wheel_y_offset = c_offset * np.sin(theta)

    # Position and orientation transformations for the wheels
    left_wheel_x = robot_x - wheel_y_offset
    left_wheel_y = robot_y + wheel_x_offset
    right_wheel_x = robot_x + wheel_y_offset
    right_wheel_y = robot_y - wheel_x_offset


    # Draw wheels
    # Create transformation for orientation
    t = transforms.Affine2D().rotate_around(left_wheel_x, left_wheel_y, theta)
    left_wheel = patches.Rectangle((left_wheel_x - wheel_height / 2, left_wheel_y - wheel_width / 2),
                                   wheel_height, wheel_width, color='black', fill=True, transform=t + ax.transData)

    t = transforms.Affine2D().rotate_around(right_wheel_x, right_wheel_y, theta)
    right_wheel = patches.Rectangle((right_wheel_x - wheel_height / 2, right_wheel_y - wheel_width / 2),
                                    wheel_height, wheel_width, color='black', fill=True, transform=t + ax.transData)

    ax.add_patch(left_wheel)
    ax.add_patch(right_wheel)

    # Draw orientation line
    line_length = robot_diameter
    end_x = robot_x + line_length * np.cos(theta)
    end_y = robot_y + line_length * np.sin(theta)
    ax.plot([robot_x, end_x], [robot_y, end_y], 'k-')

    # Plot trailer
    trailer_circle = plt.Circle((trailer_x, trailer_y), trailer_diameter/2, color='green', fill=True)
    ax.add_patch(trailer_circle)

    # Plot link
    ax.plot([robot_x, trailer_x], [robot_y, trailer_y], color='red', linewidth=2)

def animate(frame):
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')

    # Plot robot path
    plt.plot(robot_state[0,:frame], robot_state[1,:frame], 'k:')

    plot_system(robot_state[:, frame], trailer_positions[:, frame])

    ax.set_title(f"Time: {frame * dt:.2f} s")

ani = animation.FuncAnimation(fig, animate, frames=steps, interval=dt*1000)

plt.show()
