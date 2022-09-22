
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from sklearn import linear_model, tree, neighbors
from sklearn.neighbors import KNeighborsRegressor
from data.preprocessor import df3, X3, X2, X_train, y_train, X_test, y_test, x_range

# Dec
models = {'Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor}

def cb2(app):
    # Update
    @app.callback(
        Output(component_id='graph_21', component_property='figure'),
        Input(component_id='ml_dropdown', component_property='value')
    )
    # Callback definitions
    # ML Regression with prediction trace, predicting future growth
    # Plot points on scatter chart with "Regression", "Decision Tree", "k-NN"
    def reg_tree_kNN(modelType):

        # Obtain the model type to display
        model = models[modelType]()
        # Fit data to the model
        model.fit(X_train, y_train)

        # Linear array from min-max, by interval
        x_range = np.linspace(X2.min(), X2.max(), 100)
        # Predict output from reshaped array
        y_range = model.predict(x_range.reshape(-1, 1))

        # Plot with 3 curves using training set, test set and predicted values
        fig = go.Figure([
            # Training data
            go.Scatter(x=X_train.squeeze(), y=y_train,
                       name='train', mode='markers'),
            # Test data
            go.Scatter(x=X_test.squeeze(), y=y_test,
                       name='test', mode='markers'),
            # Prediction line
            go.Scatter(x=x_range, y=y_range,
                       name='prediction')
        ])
        # Return fig to Output
        return fig

    # Update
    @app.callback(
        Output(component_id='graph_22', component_property='figure'),
        Input(component_id='ml_dropdown', component_property='value')
    )
    # Callback definitions
    # Plot points on scatter chart
    # k-Nearest Neighbors. When you perform a prediction on a new sample, this model either takes the weighted
    # or un-weighted average of the neighbors. In order to see the difference between those two averaging options,
    # we train a kNN model with both of those parameters, and we plot them in the same way as the previous graph..
    # k-Nearest Neighbors
    def kNNR_plot(modelType):

        # Model #1
        # No. of neighbours, weight function type
        knn_dist = KNeighborsRegressor(10, weights='distance')
        knn_dist.fit(X3, df3.tip) # Fit training data X and target data dataframe by distance
        y_dist = knn_dist.predict(x_range.reshape(-1, 1)) # Reshape dataset & predict target data

        # Model #2
        # No. of neighbours, weight function type
        knn_uni = KNeighborsRegressor(10, weights='uniform')
        knn_uni.fit(X3, df3.tip) # Fit training data X and target data dataframe by uniform
        y_uni = knn_uni.predict(x_range.reshape(-1, 1)) # Reshape dataset & predict target data

        # Plot scatter
        fig = px.scatter(df3, x='total_bill', y='tip', color='sex', opacity=0.65)
        # Add traces for above weights types
        fig.add_traces(go.Scatter(x=x_range, y=y_uni, name='Weights: Uniform'))
        fig.add_traces(go.Scatter(x=x_range, y=y_dist, name='Weights: Distance'))
        # fig.show()

        # Return fig to Output
        return fig





