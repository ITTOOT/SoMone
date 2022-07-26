# -*- coding: utf-8 -*-

# Dash
# With html, Dash Core Components and Input & Output for callback functions
from dash import dcc, html
from data.preprocess import df

# CSS
selected_style = {
'borderTop': '1px solid #d6d6d6',
'borderBottom': '1px solid #d6d6d6',
'backgroundColor': '#119DFF',
'color': 'white',
'padding': '6px'
}

################################# DASHBOARD #################################
# Dashboard components
# options: the options the geography has, value: staring option

geo_dropdown = dcc.Dropdown(id='geo_dropdown',
                            options=df['geography'].unique(),
                            value='New York')

tabMenuBar = dcc.Tabs(id="tabsMenuBar", value='tab-1', className="os-tab-container", children=[
                dcc.Tab(label='Tab 1', value='tab-1', className='os-tab', selected_style=selected_style),
                dcc.Tab(label='Tab 2', value='tab-2', className='os-tab', selected_style=selected_style),
                dcc.Tab(label='Tab 3', value='tab-3', className='os-tab', selected_style=selected_style),
                dcc.Tab(label='Tab 4', value='tab-4', className='os-tab', selected_style=selected_style),
            ],
                style={
                'fontFamily': 'system-ui'
            },
                content_style={
                'borderLeft': '1px solid #d6d6d6',
                'borderRight': '1px solid #d6d6d6',
                'borderTop': '0px solid #d6d6d6',
                'borderBottom': '0px solid #d6d6d6',
                'padding': '0px'
            },
                parent_style={
                'maxWidth': 'auto',
                'margin': '0 auto'
            })

# Dashboard
layout = html.Div(children=[
    # Dash Components as 'children'
    html.H1(children='Avocado Prices Dashboard'),
    # Tab Panel tabsMenuBarContent
    tabMenuBar,
    html.Div(id='tabsMenuBarContent'),
])

