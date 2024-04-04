from die import Die
import plotly.express as px

die = Die()
die2 = Die(10)
results = []

for num_roll in range(50_000):
    result = die.roll() + die2.roll()
    results.append(result)

frequencies = []
max_results = die.numsides + die2.numsides
poss_results = range(2, max_results + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = 'Results of rolling D6 and a D10  50,000 times!'
labels ={'x':'Results', 'y':'Frequencfy of Results'}
fig = px.bar(x=poss_results,y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

# fig.write_html('dice_visual_D6D10.html')
fig.show()