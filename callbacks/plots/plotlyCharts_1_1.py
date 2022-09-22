#
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Output, Input
from data.preprocessor import X0

# Dec
dataFrame = X0
fp = 3 # Focal point
annotation = {"x": 'date',
                 "y": 'average_price',
                 "size": 300,
                 "color": 'average_price',
                 "title": f'Original points in '}

def cb1_1(app):
    # Update line
    @app.callback(
        Output(component_id='graph_111', component_property='figure'),
        Input(component_id='ml_dropdown', component_property='value')
    )
    # Callback definitions
    # Update graph with the Input value
    def scatter_points(modelType):
        # Filter inputs
        # filtered_df = df[df['geography'] == selected_geography]

        # annotation[1].hove_name = X.sh
        # annotation[1].hover_data = X.sh

        # calculating difference between high and low for setting bar height
       # diff = [h - l for h, l in zip(dataFrame, fp)]



        # Plot
        # fig = px.scatter(X0,
        #                 x=annotation["x"],
        #                 y=annotation["y"],
        #                 color=annotation["color"],
        #                 title=annotation["title"]
        #                 )

        fig = px.scatter(df5, x="sepal_width", y="sepal_length", color="species",
                         title="Using The add_trace() method With A Plotly Express Figure")

        # Add trace
        fig.add_trace(
            go.Scatter(
                x=[2, 4],
                y=[4, 8],
                mode="lines",
                line=go.scatter.Line(color="gray"),
                showlegend=False)
        )

        # Return fig to Output
        return fig

