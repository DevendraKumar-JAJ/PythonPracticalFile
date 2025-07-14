import matplotlib.pyplot as plt

# List of numbers
numbers = [12, 15, 18, 20, 22, 25, 30, 35, 40, 45, 50]

# Create a histogram
plt.hist(numbers, bins=6, edgecolor='black')

# Set title and labels
plt.title('Histogram of Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()

print(help(plt))