import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('dark_background')
    fix, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s= 1, c=point_numbers, cmap=plt.cm.Blues)
    ax.scatter(0,0, color='green', s= 10)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], color= 'red', s=10)
    ax.set_aspect('equal')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input('make another walk?(y/n)')
    if keep_running == 'n':
        break