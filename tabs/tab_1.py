#
from dash import html, Output, Input, dcc

from layouts.mainDashboard import geo_dropdown

def tab_1():
    return html.Div([
        html.H3('Tab content 1'),
        # Dropdown
        geo_dropdown,
        # Chart
        html.Div([
            dcc.Graph(id='price-graph_1')
        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
        # Chart
        html.Div([
            dcc.Graph(id='price-graph_2'),
            dcc.Graph(id='price-graph_3'),
        ], style={'display': 'inline-block', 'width': '49%'}),
    ])


