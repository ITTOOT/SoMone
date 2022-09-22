# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:32:30 2022

@author: player_1

Title: Plotly Tutorial Real Python

Open terminal to run by typing in the command> python nameOfFile.py
python DashTestAvocado.py

Running on Dash default URL: http://127.0.0.1:8050/
"""
# Dash
# With html, Dash Core Components and Input & Output for callback functions
# from dash import Dash, html, dcc, Input, Output
from dash import Dash
from callbacks.plots.plotlyCharts_1 import cb1
from callbacks.plots.plotlyCharts_2 import cb2
from callbacks.plots.plotlyCharts_1_1 import cb1_1
from callbacks.UxD.navigation import tab_callbacks
from layouts.mainDashboard import layout

# Dash object
app = Dash(__name__)
# Layout
app.layout = layout
# Callbacks
tab_callbacks(app)
cb1(app)
cb2(app)
cb1_1(app)



# Run app on local server @ http://127.0.0.1:8050/
if __name__ == "__main__":
    app.run_server(debug=False)
