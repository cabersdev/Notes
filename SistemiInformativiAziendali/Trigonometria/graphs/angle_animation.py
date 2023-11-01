import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation 
import sympy as sp

# functions that convert a degrees to radiant
def degrees_to_radiant(degrees):
    return (degrees * np.pi / 180)

r_start = 0 #[gr]
r_end = 360 #[gr]
r_interval = 10

# creating an array that rappresent the rradiant
degreesArr = np.arange(r_start,r_end+r_interval,r_interval)

# convert the value in radiant 
radiantArr = degrees_to_radiant(degreesArr)

# define figure
fig = plt.figure(figsize=(20,20),dpi=120,facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(1,1)

ax = fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))

# define the radius of the circumference
radius = 1

# define the origin 
center = (0,0)

# Generate theta values from 0 to 2*pi to create a circle
theta = np.linspace(0, 2*np.pi, 100)

# Calculate the x and y coordinates of the points on the circumference
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

circumference = ax.plot(x,y)

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.axis('equal')


# Function to update the plot
def updatePlot(frame):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('equal')
    ax.plot(x, y)  # Plot the circle
    
    # Plot lines representing angles in radians for the current frame
    angle = radiantArr[frame]
    end_x = center[0] + radius * np.cos(angle)
    end_y = center[1] + radius * np.sin(angle)
    ax.plot([center[0], end_x], [center[1], end_y], color='green', linewidth=2)

    # Add textbox with angle number in the upper right corner
    angle_text = f'Angle: {degreesArr[frame]}°'
    ax.text(0.95, 0.95, angle_text, transform=ax.transAxes,
            ha='right', va='top', bbox=dict(facecolor='white', alpha=0.5))


    # Calculate the symbolic representation of the angle in radians using Sympy
    angle_fraction = sp.Rational(angle / np.pi).limit_denominator(1000)  
    # get a fraction of the angle in terms of pi
    angle_symbolic_text = r'$\theta = {} \pi$'.format(angle_fraction)
    ax.text(0.95, 0.89, angle_symbolic_text, transform=ax.transAxes,
            ha='right', va='top', bbox=dict(facecolor='white', alpha=0.5))


    
frameAmount = len(radiantArr)

# animation

angleAnimation = animation.FuncAnimation(fig,updatePlot,
                                         frames=frameAmount,interval=1000,
                                         repeat=True,blit=True
                                         )


# Save the animation as a GIF file
angleAnimation.save('/home/caber/Notes/SistemiInformativiAziendali/Trigonometria/graphs/angle_animation.gif', writer='imagemagick')

plt.show()
