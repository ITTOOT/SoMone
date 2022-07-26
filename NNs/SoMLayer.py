"""
Example using simple SOM to cluster sklearn's Iris dataset.

NOTE: This example uses sklearn and matplotlib, but neither is required to use
the som (sklearn is used here just for the data and matplotlib just to plot
the output).

@author: Riley Smith
Created: 2-1-2021
"""

from sklearn import datasets
from sklearn_som.som import SOM

# Get the first 2 features from the iris dataset in sklearn
iris = datasets.load_iris()
iris_data = iris.data[:, :2]
iris_label = iris.target

# 3x1 SOM (3 clusters) instance with the classes from the dataset
# MxN matrix - m = dim 0 (vertical), n = dim 0 (horizontal)
# dim = dimensions of the input
# lr = weights update step size
iris_som = SOM(m=3, n=1, dim=2)

# Fit the data to the SoM
iris_som.fit(iris_data)

# Assign each datapoint to a predicted cluster
predictions = iris_som.predict(iris_data)
