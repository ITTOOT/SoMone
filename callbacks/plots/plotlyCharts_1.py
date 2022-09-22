#
import plotly.express as px
from dash.dependencies import Output, Input
from data.preprocessor import df1

def cb1(app):
    # Update line
    @app.callback(
        Output(component_id='graph_11', component_property='figure'),
        Input(component_id='geo_dropdown', component_property='value')
    )
    # Callback definitions
    # Update graph with the Input value
    def update_line(selected_geography):
        # Filter inputs
        filtered_df = df1[df1['geography'] == selected_geography]
        # Plot
        plot = px.line(filtered_df,
                           x='date',
                           y='average_price',
                           color='type',
                           title=f'Avocado Prices in {selected_geography}')
        # Return fig to Output
        return plot

    #
    # Update scatter
    @app.callback(
        Output(component_id='graph_12', component_property='figure'),
        Input(component_id='geo_dropdown', component_property='value')
    )
    # Callback definitions
    # Update graph with the Input value
    def update_line(selected_geography):
        # Filter inputs
        filtered_df = df1[df1['geography'] == selected_geography]
        # Plot
        plot = px.line(filtered_df,
                           x='date',
                           y='average_price',
                           color='type',
                           title=f'Avocado Prices in {selected_geography}')
        # Return fig to Output
        return plot

    #
    # Update scatter
    @app.callback(
        Output(component_id='graph_13', component_property='figure'),
        Input(component_id='geo_dropdown', component_property='value')
    )
    # Callback definitions
    # Update graph with the Input value
    def update_bubble(selected_geography):
        # Filter inputs
        filtered_df = df1[df1['geography'] == selected_geography]
        # Plot
        plot = px.line(filtered_df,
                           x='date',
                           y='average_price',
                           color='type',
                           title=f'Avocado Prices in {selected_geography}')
        # Return fig to Output
        return plot