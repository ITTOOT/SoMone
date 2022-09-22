#
from dash import html, Output, Input
from tabs import tab_1, tab_2, tab_3, tab_4


def tab_callbacks(app):
    # Render tab bar
    @app.callback(
        Output(component_id='tabsMenuBarContent', component_property='children'),
        Input(component_id='tabsMenuBar', component_property='value'))
    # Callback definitions
    def render_content(tab):
        if tab == 'tab-1':
            return tab_1.tab_1()
        elif tab == 'tab-2':
            return tab_2.tab_2()
        elif tab == 'tab-3':
             return tab_3.tab_3()
        elif tab == 'tab-4':
             return tab_4.tab_4()


