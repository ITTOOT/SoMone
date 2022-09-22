# Load packages
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.model_selection import train_test_split

# Dec

# Prepare data
# Dataset - Save in same directory as the script to avoid using PATH
df1 = pd.read_csv('../datasets/avocado-updated-2020.csv')

# Check data
df1.info()
# print(df['type'].value_counts(dropna=False))
# print(df['geography'].value_counts(dropna=False))

# Plot
# Filter data frame
# msk = df['geography'] == 'Los Angeles'
# Chart
# px.line(df[msk], x='date', y='average_price', color='type')

# Train & test data
df2 = px.data.tips()  # replace with your own data source
X2 = df2.total_bill.values[:, None]
X_train, X_test, y_train, y_test = train_test_split(X2, df2.tip, random_state=42)

# Train & test data
df3 = px.data.tips()
X3 = df3.total_bill.values.reshape(-1, 1)
x_range = np.linspace(X3.min(), X3.max(), 100)

# Train & test data
mesh_size = .02
margin = 0
df4 = px.data.iris()
X4 = df4[['sepal_width', 'sepal_length']]
y4 = df4['petal_width']

# SciKit test files
from sklearn.datasets import make_classification

# Create clusters of points normally distributed (std=1)
# about vertices of an n_informative-dimensional hypercube
# with sides of length 2*class_sep and assigns an equal number
# of clusters to each class. It introduces interdependence
# between these features and adds various types of further noise to the data.
#
# samples=X, labels=y
X0, y0 = make_classification(
    n_samples=9,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_classes=3,
    n_clusters_per_class=1,
    class_sep=1.0,
    random_state=0,
)
# Check data
print(X0)















