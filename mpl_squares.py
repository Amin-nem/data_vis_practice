import matplotlib.pyplot as plt
squares = [i**2 for i in range(25000)]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()