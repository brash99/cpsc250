import matplotlib.pyplot as plt
import pandas as pd

file = input()

# TODO: Read in CSV file as a dataframe
broadway_show_plot = pd.read_csv(file)

# TODO: Insert a column to the dataframe as the last column
#       Label the column "Size", which contains half the values in column "Gross Potential"

broadway_show_plot['Size']  = broadway_show_plot['Gross Potential'] / 2 #Chatgpt gave me this syntax

# TODO: Output dataframe
print(broadway_show_plot)

# TODO: Create scatter plot
plt.scatter(broadway_show_plot['Gross Potential'], broadway_show_plot['Capacity'],marker='x',color='orange',s=broadway_show_plot['Size'])


# TODO: Add axis labels and title
plt.xlabel("Capacity", fontsize=10)
plt.ylabel("Gross Potential", fontsize=10)
plt.title("Gross Potential vs Capacity", fontsize=16)

# TODO: Add gridlines
plt.grid(linestyle='--')

# TODO: Save figure as output_fig.png
plt.show()
plt.savefig("output_fig.png") #Chatgpt gave me this syntax