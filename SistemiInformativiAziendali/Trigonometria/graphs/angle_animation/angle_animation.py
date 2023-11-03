import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import sympy as sp

# functions that convert degrees to radians
def degrees_to_radians(degrees):
    return (degrees * np.pi / 180)

r_start = 0  # [degrees]
r_end = 360  # [degrees]
r_interval = 10

# creating an array that represents the degrees
degreesArr = np.arange(r_start, r_end + r_interval, r_interval)

# convert the values to radians
radianArr = degrees_to_radians(degreesArr)

# define figure
fig = plt.figure(figsize=(8, 8), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(1, 1)

ax = fig.add_subplot(gs[0, :], facecolor=(0.9, 0.9, 0.9))

# define the radius of the circumference
radius = 1

# define the origin
center = (0, 0)

# Generate theta values from 0 to 2*pi to create a circle
theta = np.linspace(0, 2 * np.pi, 100)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

circumference, = ax.plot(x, y)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('equal')

# Function to update the plot
def updatePlot(frame):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('equal')
    ax.plot(x, y)  # Plot the circle
    
    # Plot lines representing angles in radians for the current frame
    angle = radianArr[frame]
    end_x = center[0] + radius * np.cos(angle)
    end_y = center[1] + radius * np.sin(angle)
    ax.plot([center[0], end_x], [center[1], end_y], color='red', linewidth=2)

    # Calculate the angle in radians using Sympy
    angle_radians = sp.Rational(angle).evalf()  # Convert the angle to a rational number and evaluate it
    # Add textbox with angle number in the upper right corner
    angle_degrees = degreesArr[frame]
    angle_text = f'Angle: {angle_degrees}°'
    ax.text(0.95, 0.95, angle_text, transform=ax.transAxes,
            ha='right', va='top', bbox=dict(facecolor='white', alpha=0.5))

    # Calculate the symbolic representation of the angle in radians using Sympy
    angle_fraction = sp.Rational(angle / np.pi).limit_denominator(1000)  # Get a fraction of the angle in terms of pi
    angle_symbolic_text = r'$\theta = {} \pi$'.format(angle_fraction)
    ax.text(0.95, 0.89, angle_symbolic_text, transform=ax.transAxes,
            ha='right', va='top', bbox=dict(facecolor='white', alpha=0.5))

# Number of frames in the animation
frameAmount = len(radianArr)

# Animation
angleAnimation = animation.FuncAnimation(fig, updatePlot,
                                         frames=frameAmount, interval=1000,
                                         repeat=True, blit=False)

# Save the animation as a GIF file
angleAnimation.save('/home/caber/Notes/SistemiInformativiAziendali/Trigonometria/graphs/angle_animation/angle_animation.gif', writer='imagemagick')

plt.show()

