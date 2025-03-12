import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Create a random walk with 5,000 points to simulate molecular motion.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Set the plot style and create a figure with axes.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    
    # Plot the points as a continuous line to simulate fluid motion.
    ax.plot(rw.x_values, rw.y_values, linewidth=1, color='blue')
    ax.set_aspect('equal')

    # Emphasize the starting and ending points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # Start point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # End point

    # Remove the axes to improve visualization.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # Display the plot.
    plt.show()

    # Ask the user if they want to generate another walk.
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break



# 15-3. Molecular Motion: Modify rw_visual.py by replacing ax.scatter() with
# ax.plot(). To simulate the path of a pollen grain on the surface of a drop of
# water, pass in the rw.x_values and rw.y_values, and include a linewidth argument. Use 5,000 instead of 50,000 points to keep the plot from being too busy.