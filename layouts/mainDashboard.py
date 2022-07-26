# -*- coding: utf-8 -*-

# Dash
# With html, Dash Core Components and Input & Output for callback functions
from dash import dcc, html
from data.preprocess import df

################################# DASHBOARD #################################
# Dashboard components
# options: the options the geography has, value: staring option

geo_dropdown = dcc.Dropdown(id='geo_dropdown',
                            options=df['geography'].unique(),
                            value='New York')

tabMenuBar = dcc.Tabs(id="tabsMenuBar", value='tab-1', children=[
    dcc.Tab(label='Tab 1', value='tab-1', style='tab_style', selected_style='tab_selected_style'),
    dcc.Tab(label='Tab 2', value='tab-2', style='tab_style', selected_style='tab_selected_style'),
    dcc.Tab(label='Tab 3', value='tab-3', style='tab_style', selected_style='tab_selected_style'),
    dcc.Tab(label='Tab 4', value='tab-4', style='tab_style', selected_style='tab_selected_style'),
], style='tabs_styles')

# Dashboard
layout = html.Div(children=[
    # Dash Components as 'children'
    html.H1(children='Avocado Prices Dashboard'),
    # Tab Panel tabsMenuBarContent
    tabMenuBar,
    html.Div(id='tabsMenuBarContent'),
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
