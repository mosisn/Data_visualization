import matplotlib.pyplot as plt


x = range(1, 1001)
y = [x**2 for x in x]

plt.style.use('dark_background')
fix, ax = plt.subplots()
# ax.scatter(x, y, s=10, c = x, cmap=plt.cm.Blues)
ax.scatter(x, y, s=10, color ='red')

ax.set_xlabel('value', fontsize = 14)
ax.set_title('square numbers', fontsize = 24)
ax.set_ylabel('square of value', fontsize = 14)
ax.tick_params(labelsize = 14)
ax.ticklabel_format(style='plain')

ax.axis([0, 1100, 0, 1_100_000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()