import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation 

# functions that convert a degrees to radiant
def degrees_to_radiant(degrees):
    return (degrees * np.pi / 180)

r_start = 0 #[gr]
r_end = 360 #[gr]
r_interval = 0.005

# creating an array that rappresent the rradiant
degreesArr = np.arange(r_start,r_end+r_interval,r_interval)

# convert the value in radiant 

radiantArr = degrees_to_radiant(degreesArr)

radius = 5

# calculate x and y coordinates of the circumference
x_circumference = radius * np.cos(radiantArr)
y_circumference = radius * np.sin(radiantArr)

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(1,1)
ax = fig.add_subplot(gs[0:],facecolor=(0.9,0.9,0.9))

# plot the circumference
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.plot(x_circumference, y_circumference, color='b', linewidth=2)


plt.show()

