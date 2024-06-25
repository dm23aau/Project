# -*- coding: utf-8 -*-
"""Electric Vehicle Charging Infrastructure.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18iqbxiabeHjMB9bQRQWU5p1aM3241QZY
"""

# Required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
import numpy as np
import seaborn as sns

# Load the dataset from the uploaded location
file_path ='station_data_dataverse.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset and check for missing values and data types
print("Shape of the dataset:")
print(data.shape)

data_head = data.head()
print("First 5 rows of the dataset:")
print(data_head)

missing_values = data.isnull().sum()
print("Number of Missing values in the dataset, column wise:")
print(missing_values)

data_types = data.dtypes
print("Data types of each column:")
print(data_types)

# 'distance' column has a lot of missing values.
# Plot the distribution of the 'distance' column
plt.figure(figsize=(10, 6))
plt.hist(data['distance'].dropna(), bins=100, color='blue', alpha=0.7)
plt.title('Distribution of Distance Values')
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Remove rows where 'distance' is missing
cleaned_data = data.dropna(subset=['distance'])

# Print the shape of the data before and after removal of missing values to see how many rows were dropped
print("Original Data Shape:", data.shape)
print("Cleaned Data Shape:", cleaned_data.shape)
