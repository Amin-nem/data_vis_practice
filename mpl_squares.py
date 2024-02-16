import matplotlib.pyplot as plt
squares = [i**2 for i in range(-2500,2501)]
fig, ax = plt.subplots()
ax.plot(squares,linewidth=3)

# title and axes' label
ax.set_title('Square Numbers',fontsize=24,color='red')
ax.set_xlabel('Value',fontsize=24)
ax.set_ylabel('Square of Value',fontsize=24)

# size of tick labels
ax.tick_params(labelsize=14)
plt.show()