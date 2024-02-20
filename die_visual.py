import plotly.express as px

from die import Die
# Create a D6

die = Die()
# roll and store the resutls
results =[die.roll() for i in range(1000)]

# Analyze the results
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize
fig = px.bar(x=poss_results,y=frequencies)
fig.show()