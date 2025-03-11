import matplotlib.pyplot as plt

# First plot with first 5 cubic numbers
plt.style.use('seaborn-v0_8')
# Create a figure and two subplots (ax1 and ax2) arranged in 1 row and 2 columns
# figsize=(15, 6) sets the size of the entire figure to 15 inches by 6 inches
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# First plot - 5 cubic numbers
# Create data for first 5 numbers (1-5)
x_values_small = range(1, 6)
# Calculate cube of each number using list comprehension
y_values_small = [x**3 for x in x_values_small]

# Create scatter plot: x and y coordinates from our data,
# c=y_values_small colors points based on y-values using Blues colormap,
# s=40 sets the size of each point to 40
ax1.scatter(x_values_small, y_values_small, c=y_values_small, cmap=plt.cm.Blues, s=40)
# Set the title and font size
ax1.set_title("First 5 Cubic Numbers", fontsize=14)
# Label x-axis
ax1.set_xlabel("Value", fontsize=12)
# Label y-axis 
ax1.set_ylabel("Cube of Value", fontsize=12)
# Set font size for tick labels
ax1.tick_params(labelsize=12)

# Second plot - 5000 cubic numbers
x_values_large = range(1, 5001)
y_values_large = [x**3 for x in x_values_large]

ax2.scatter(x_values_large, y_values_large, c=y_values_large, cmap=plt.cm.Reds, s=10)
ax2.set_title("First 5,000 Cubic Numbers", fontsize=14)
ax2.set_xlabel("Value", fontsize=12)
ax2.set_ylabel("Cube of Value", fontsize=12)
ax2.tick_params(labelsize=12)

# Format the larger plot to use scientific notation
ax2.ticklabel_format(style='sci')

plt.tight_layout()
plt.show()