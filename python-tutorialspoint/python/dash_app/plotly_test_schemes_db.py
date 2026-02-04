import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

import plotly.express as px
import plotly.graph_objects as graph_objects
import plotly.io as pio

print(pio.templates)

theme = ['ggplot2', 'seaborn', 'simple_white', 'plotly',
         'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
         'ygridoff', 'gridon', 'none']

for theme in theme: 
    fig = graph_objects.Figure()
    fig.add_scatter(x=[1,2,3,4,5], y=[2,3,4,5,6])
    fig.add_scatter(x=[6,5,4,3,2], y=[7,3,5,4,6])
    fig.layout.title = f'Theme = {theme}'
    fig.layout.xaxis.title = 'The X-Axis'
    fig.layout.yaxis.title = 'The Y-Axis'
    fig.layout.template = theme
    fig.layout.height = 350
    fig.show()
    
