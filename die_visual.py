import plotly.express as px

from die import Die

# Create a D6
die1 = Die()
die2 = Die()

# roll and store the resutls
result1 =[die1.roll() for i in range(3000)]
result2 =[die2.roll() for i in range(3000)]
results = [i+j for i,j in zip(result1,result2)]

# Analyze the results
frequencies = []
poss_results = range(2, die1.num_sides + die2.num_sides +1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize
fig = px.bar(x=poss_results,y=frequencies,title='results of rolling two D6 3000 times',labels={'x':'results','y':'frequency'})
fig.show()