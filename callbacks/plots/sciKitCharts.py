
from dash.dependencies import Output, Input

import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.tools as tls
from sklearn.neighbors import NeighborhoodComponentsAnalysis
from matplotlib import cm
from scipy.special import logsumexp
from data.preprocessor import X0, y0


# Neighborhood Component Analysis (NCA) is a machine learning algorithm for metric learning.
# It learns a linear transformation in a supervised fashion to improve the classification accuracy
# of a stochastic nearest neighbors rule in the transformed space.

# Dec
fp = 3 # Focal point

def plotly_callbacks(app):
    # Update
    @app.callback(
        Output(component_id='graph_210', component_property='figure'),
        Input(component_id='geo_dropdown', component_property='value')
    )
    # Callback definitions
    # scatter_points
    # Plot points on scatter chart
    def scatter_points(selected_geography):
        # MatPloLib plot figure...
        plt.figure(1)
        # GCA - Get the current axes from the plot figure and add formatting to its ax
        ax = plt.gca()

        # Formatting axes of elements into labeled points
        for i in range(X0.shape[0]):
            # Add text to the points at each index at the center of coords x= X[i, 0], y= X[i, 1]
            ax.text(X0[i, 0], X0[i, 1], str(i), va="center", ha="center")
            # Scatter plot points at coords= x, y, s=size, c=colour, alpha= transparency
            ax.scatter(X0[i, 0], X0[i, 1], s=300, c=cm.Set1(y0[[i]]), alpha=0.4)

        # Plot axis formatting object = ax
        ax.set_title("Original points")
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.axis("equal")  # so that boundaries are displayed correctly as circles

        # Focal point
        i = fp
        # Invoke the focal point X = data, i = focal point, ax = axes
        # All links generated from here!
        relate_point(X0, i, ax)
        # Show the plot
        #plt.show()
        #plt.close()
        tls.mpl_to_plotly(plt)
        return plt.show()

    # Update
    @app.callback(
        Output(component_id='graph_220', component_property='figure'),
        Input(component_id='geo_dropdown', component_property='value')
    )
    # Callback definitions
    # update_nca
    # Update NCA (Neighborhood Components Analysis)
    def nca_points(selected_geography):
        # learn an embedding and plot the points after the transformation.
        # We then take the embedding and find the nearest neighbors.
        #
        # ML algorithm for supervised linear transformation of nearest neighbours
        nca = NeighborhoodComponentsAnalysis(max_iter=30, random_state=0)
        # Fit nca model to training data samples=X & labels=y
        nca = nca.fit(X0, y0)

        # MatPloLib plot figure...
        plt.figure(1)
        # GCA - Get the current axes from the plot figure and add formatting to its ax
        ax = plt.gca()

        # Apply the learned transformation from samples X and save as an embedded array...
        X_embedded = nca.transform(X0)
        # Focal point
        i = fp
        # Invoke the focal point X = data, i = focal point, ax = axes
        # All links generated from here!
        relate_point(X_embedded, i, ax)

        # Formatting axes of elements into labeled points
        for i in range(len(X0)):
            # Add text to the points at each index at the center of coords x= Xe[i, 0], y= Xe[i, 1]
            ax.text(X_embedded[i, 0], X_embedded[i, 1], str(i), va="center", ha="center")
            # Scatter plot points at coords= x, y, s=size, c=colour, alpha= transparency
            ax.scatter(X_embedded[i, 0], X_embedded[i, 1], s=300, c=cm.Set1(y[[i]]), alpha=0.4)

        # Plot axis formatting object = ax
        ax.set_title("NCA embedding")
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.axis("equal") # so that boundaries are displayed correctly as circles
        # Show the plot
        # plt[2].show()
        # plt[2].close()

        return plt

    #################################################
    #################### HELPERS ####################

    # link_thickness_i
    # Create and format lines to data point in X from focal point i
    def link_thickness_i(X, i):
        # Difference from i - n
        diff_embedded = X[i] - X
        # Einstein summation convention, multi-dimensional, linear algebraic array operations represented in a simple fashion.
        # "ij,ij->i" these are the arrays for the operation
        dist_embedded = np.einsum("ij,ij->i", diff_embedded, diff_embedded)
        dist_embedded[i] = np.inf  # Create an array to infinity

        # compute exponentiated distances (use the log-sum-exp trick to
        # avoid numerical instabilities), when x and y are both small numbers,
        # multiplying x times y may underflow, differentiating each function separately
        # is easier than applying the product rule.  a log probability which may be very large,
        # and either negative or positive, then exponentiating might result in under- or overflow respectively.
        exp_dist_embedded = np.exp(-dist_embedded - logsumexp(-dist_embedded))
        return exp_dist_embedded

    # relate_point
    # Position of the focal point from dataset X
    def relate_point(X, i, ax):
        # Data X element to select
        pt_i = X[i]
        # Create a link between focal point and each element in X
        for j, pt_j in enumerate(X):
            # Create thickness of links
            thickness = link_thickness_i(X, i)
            if i != j:
                line = ([pt_i, pt_j], [pt_i, pt_j])
                # Add link lines formatting to ax, using link_thickness_i()
                ax.plot(*line, c=cm.Set1(y0[j]), linewidth=5 * thickness[j])

