import matplotlib.pyplot as plt
# style
plt.style.use('fivethirtyeight')
# data
x_values = range(-50,51)
y_values = [i**2 for i in x_values]
#plot
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,s=30)
# chat title and label
ax.set_title('Square Numbers')
ax.set_xlabel('value')
ax.set_ylabel('square of value')

# set size of tick labels
ax.tick_params(labelsize=14)

# set range for axis
ax.axis([-50,51,-100,2600])

plt.show()