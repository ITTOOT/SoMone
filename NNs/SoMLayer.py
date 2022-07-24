"""
Example using simple SOM to cluster sklearn's Iris dataset.

NOTE: This example uses sklearn and matplotlib, but neither is required to use
the som (sklearn is used here just for the data and matplotlib just to plot
the output).

@author: Riley Smith
Created: 2-1-2021
"""
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets

from sklearn_som.som import SOM