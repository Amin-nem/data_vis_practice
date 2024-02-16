import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
fig,ax = plt.subplots()
ax.scatter(2,4,s=200)

# chat title and label
ax.set_title('Square Numbers')
ax.set_xlabel('value')
ax.set_ylabel('square of value')

# set size of tick labels
ax.tick_params(labelsize=14)


plt.show()