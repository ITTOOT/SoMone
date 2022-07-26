#
from dash import html, Output, Input

def tab_callbacks(app):
    # Render tab bar
    @app.callback(
        Output(component_id='tabsMenuBarContent', component_property='children'),
        Input(component_id='tabsMenuBar', component_property='value'))
    # Callback definitions
    def render_content(tab):
        if tab == 'tab-1':
            return html.Div([
                html.H3('Tab content 1')
            ])
        elif tab == 'tab-2':
            return html.Div([
                html.H3('Tab content 2')
            ])
        elif tab == 'tab-3':
            return html.Div([
                html.H3('Tab content 3')
            ])
        elif tab == 'tab-4':
            return html.Div([
                html.H3('Tab content 4')
            ])

