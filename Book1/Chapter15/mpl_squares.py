# Import matplotlib library which is used for creating graphs and plots
import matplotlib.pyplot as plt

# squares: contains the square of each number in input_values
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Set the visual style of the plot to 'seaborn', which is a more modern look
plt.style.use('seaborn-v0_8')

# Create a new figure (window) and axes (the actual plot)
# fig is the entire figure/window
# ax is the plot itself
fig, ax = plt.subplots()

# Create the line plot:
# - input_values will be on x-axis
# - squares will be on y-axis
# - linewidth=3 makes the line thicker
# - color='red' sets the line color to red
ax.plot(input_values, squares, linewidth=3, color='red')

# Add a title to the plot with font size 24
ax.set_title("Square Numbers", fontsize=24)

# Label the x-axis and y-axis with font size 14
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the size of the numbers on both axes to font size 14
ax.tick_params(labelsize=14)

# Display the plot in a window
plt.show()