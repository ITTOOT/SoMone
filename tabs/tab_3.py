#
from dash import html, Output, Input, dcc

from layouts.mainDashboard import ml_dropdown_1

tabTitle = 'Tab content 3'
plotId = ['graph_0', 'graph_111', 'graph_112', 'graph_113']
dropdown = ml_dropdown_1

def tab_3():
    return html.Div([
        html.H3(tabTitle),
        # Dropdown
        dropdown,
        # Chart
        html.Div([
            dcc.Graph(id=plotId[1])
        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 2000'}),
        # Chart
        html.Div([
            dcc.Graph(id=plotId[2]),
            dcc.Graph(id=plotId[3]),
        ], style={'display': 'inline-block', 'width': '49%'}),
    ])


