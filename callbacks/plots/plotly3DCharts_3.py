
from dash.dependencies import Output, Input

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.svm import SVR
from data.preprocessor import df, X, y, margin, mesh_size


def plotly_callbacks(app):
    # Update
    @app.callback(
        Output(component_id='graph_23', component_property='figure'),
        Input(component_id='geo_dropdown', component_property='value')
    )
    # Callback definitions
    # Visualize the decision plane of your model whenever you have more than one variable in your input data.
    # Here, we will use sklearn.svm.SVR, which is a Support Vector Machine (SVM) model specifically designed for regression.
    # 3D regression surface with px.scatter_3d and go.Surface
    def scatter3D(name):
        # Condition the model on sepal width and length, predict the petal width
        model = SVR(C=1.)
        model.fit(X[4], y[4])

        # Create a mesh grid on which we will run our model
        x_min, x_max = X[4].sepal_width.min() - margin, X[4].sepal_width.max() + margin
        y_min, y_max = X[4].sepal_length.min() - margin, X[4].sepal_length.max() + margin
        xrange = np.arange(x_min, x_max, mesh_size)
        yrange = np.arange(y_min, y_max, mesh_size)
        xx, yy = np.meshgrid(xrange, yrange)

        # Run model
        pred = model.predict(np.c_[xx.ravel(), yy.ravel()])
        pred = pred.reshape(xx.shape)

        # Generate the plot
        fig = px.scatter_3d(df[4], x='sepal_width', y='sepal_length', z='petal_width')
        fig.update_traces(marker=dict(size=5))
        fig.add_traces(go.Surface(x=xrange, y=yrange, z=pred, name='pred_surface'))
        #fig.show()

        return fig






