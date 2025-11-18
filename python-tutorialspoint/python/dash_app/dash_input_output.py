import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

import plotly.express as px

# See https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



country = ['England', 'Ireland', 'Scotland', 'Wales']

app.layout = html.Div([
    dcc.Dropdown(
        id='country_dropdown',
        options=[{'label': c, 'value': c} for c in country],   #list comprehension 
        placeholder='Select a country',
        clearable=True
    ),
    html.Br(), #HTML line break. 
    html.Div(id='country_output')
])


#Callbacks
#Callback functions are decorators. Output definitions must come first before input definitions. 
@app.callback(Output('country_output', 'children'),
              Input('country_dropdown', 'value'))
def display_country(country):
    if not country:
        return 'Please select a country.'
    return f'I would like to visit {country}.'
   


if __name__ == '__main__':
    app.run(debug=True, port=8181)