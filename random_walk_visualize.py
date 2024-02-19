import matplotlib.pyplot as plt

from random_walk import RandomWalk

# let's make a random walk

rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fix, ax = plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s=15)
ax.set_aspect('equal')
plt.show()