import matplotlib.pyplot as plt 
import numpy as np 

# define the figure
fig = plt.figure(figsize=(10,10),dpi=120,facecolor=(0.8,0.8,0.8))

ax = fig.add_subplot(facecolor=(0.9, 0.9, 0.9))

# define the radius of the circumference
radius = 1

# define the origin
center = (0, 0)

# Generate theta values from 0 to 2*pi to create a circle
theta = np.linspace(0, 2 * np.pi, 100)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

circumference, = ax.plot(x, y)

# plotting the x and y axes
ax.axhline(0, color='black', linewidth=1)  # horizontal line (x-axis)
ax.axvline(0, color='black', linewidth=1)  # vertical line (y-axis)



# Points where circumference touches the axes
points = [(1, 0), (0, 1), (-1, 0), (0, -1)]
labels = ['(1, 0)', '(0, 1)', '(-1, 0)', '(0, -1)']

# Adding text boxes for the points
for point, label in zip(points, labels):
    ax.plot(point[0], point[1], 'ko')  # plot the point
    ax.text(point[0], point[1], label, ha='right', va='bottom')  # add the text box

# Adding text box for the origin (0, 0)
ax.plot(0, 0, 'ko')  # plot the origin point
ax.text(0, 0, '(0, 0)', ha='right', va='bottom')  # add the text box

# setting up the ax
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('equal')

# Save the figure as a PNG file
plt.savefig('/home/caber/Notes/SistemiInformativiAziendali/Trigonometria/graphs/goniometric_circumference/goniometric_cir_plot.png')

plt.show()
