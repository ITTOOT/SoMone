# Load packages
import pandas as pd

# Prepare data
# Dataset - Save in same directory as the script to avoid using PATH
df = pd.read_csv('../datasets/avocado-updated-2020.csv')

# Check data
df.info()
# print(df['type'].value_counts(dropna=False))
# print(df['geography'].value_counts(dropna=False))

# Plot
# Filter data frame
# msk = df['geography'] == 'Los Angeles'
# Chart
# px.line(df[msk], x='date', y='average_price', color='type')
