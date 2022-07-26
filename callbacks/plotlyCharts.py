#
import plotly.express as px
from dash.dependencies import Output, Input
from data.preprocess import df

def plotly_callbacks(app):
    # Update line
    @app.callback(
        Output(component_id='price-graph_1', component_property='figure'),
        Input(component_id='geo_dropdown', component_property='value')
    )
    # Callback definitions
    # Update graph with the Input value
    def update_line(selected_geography):
        # Filter inputs
        filtered_df = df[df['geography'] == selected_geography]
        # Plot
        line_fig = px.line(filtered_df,
                           x='date',
                           y='average_price',
                           color='type',
                           title=f'Avocado Prices in {selected_geography}')
        # Return fig to Output
        return line_fig

    #
    #
    # Update scatter
    @app.callback(
        Output(component_id='price-graph_2', component_property='figure'),
        Input(component_id='geo_dropdown', component_property='value')
    )
    # Callback definitions
    # Update graph with the Input value
    def update_line(selected_geography):
        # Filter inputs
        filtered_df = df[df['geography'] == selected_geography]
        # Plot
        line_fig = px.line(filtered_df,
                           x='date',
                           y='average_price',
                           color='type',
                           title=f'Avocado Prices in {selected_geography}')
        # Return fig to Output
        return line_fig
