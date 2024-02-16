import matplotlib.pyplot as plt
nums = range(-100,101)

squares = [i**2 for i in range(-100,101)]
fig, ax = plt.subplots()
ax.plot(nums,squares,linewidth=3)

# title and axes' label
ax.set_title('Square Numbers',fontsize=24,color='red')
ax.set_xlabel('Value',fontsize=15)
ax.set_ylabel('Square of Value',fontsize=15)

# size of tick labels
ax.tick_params(labelsize=10)
plt.show()