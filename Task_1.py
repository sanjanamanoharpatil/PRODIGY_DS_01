import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'dataset1.csv'
data = pd.read_csv(file_path, skiprows=4)

# Select data for the year 2020 and drop rows with missing values
data_2020 = data[['Country Name', '2020']].dropna()

# Sort the values by population for better visualization
data_2020_sorted = data_2020.sort_values(by='2020', ascending=False).head(20)  # Select top 20 countries by population

# Create a bar chart to visualize the distribution of populations in 2020
plt.figure(figsize=(10, 6))
plt.barh(data_2020_sorted['Country Name'], data_2020_sorted['2020'], color='skyblue')
plt.xlabel('Population in 2020')
plt.ylabel('Country Name')
plt.title('Top 20 Countries by Population in 2020')
plt.gca().invert_yaxis()  # Invert y-axis to show the largest population at the top
plt.tight_layout()

# Show the plot
plt.show()
