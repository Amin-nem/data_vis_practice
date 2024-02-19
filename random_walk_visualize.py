import matplotlib.pyplot as plt

from random_walk import RandomWalk

# let's make a random walk

rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fix, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues, edgecolors='none',s=15)
ax.set_aspect('equal')

# Emphasize the first and the last points
ax.scatter(0,0,c='green',edgecolors='none',s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
plt.show()