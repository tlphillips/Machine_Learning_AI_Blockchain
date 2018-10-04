'''The Gapminder dataset that you worked with in previous chapters also contained a categorical 'Region' feature, 
which we dropped in previous exercises since you did not have the tools to deal with it. Now however, you do, so we have added it back in!
Your job in this exercise is to explore this feature. Boxplots are particularly useful for visualizing categorical features such as this.'''

#TASK

#Import pandas as pd.
#Read the CSV file 'gapminder.csv' into a DataFrame called df.
#Use pandas to create a boxplot showing the variation of life expectancy ('life') by region ('Region'). To do so, pass the column names in to df.boxplot() (in that order).

# # Import pandas
# ____

# # Read 'gapminder.csv' into a DataFrame: df
# df = ____

# # Create a boxplot of life expectancy per region
# df.boxplot(____, ____, rot=60)

# # Show the plot
# plt.show()




#SOLVE
# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('gm_2008_region.csv')

# Create a boxplot of life expectancy per region
df.boxplot('life', 'Region', rot=60)

# Show the plot
plt.show()
