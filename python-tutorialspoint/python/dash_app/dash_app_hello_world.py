import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

# See https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# A Div tag act as a container for other HTML tags. H1 tag is a heading tag. It stores text that represents heading on a web page. 
app.layout = html.Div([
    #This element is the argument passed into the html.Div children parameter. 
    #This string is the argument passed into the html.H1 children parameter.  
    dbc.Row([
        dbc.Col([
            html.H1('My first Dash web app!', style={'color': 'blue', 'textAlign': 'left'}),   
            html.H1('The power of Plotly & Dash'),   
            html.H2('Our first Dash app')
            ], lg=5, md=12),
        dbc.Col([
            html.P('About: '),
            html.Ul([
            html.Li('Author: Jim Morisson'),
            html.Li('Date: 01/12/2021'),
            html.Li('Course: Plotly & Dash on Udemy'),
            html.Li([
                'Course Site: ',
                html.A('Link to Course', href='https://udemy.com')  
                ]),
            ])
        ], lg=5, md=12) 
    ])
])

if __name__ == '__main__':
    app.run(debug=True)