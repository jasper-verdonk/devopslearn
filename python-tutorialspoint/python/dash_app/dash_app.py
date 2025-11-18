import dash
from dash import html
from dash import dcc


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("My First Dash App"),
    dcc.Dropdown(
        options=[
            {'label': 'Option 1', 'value': '1'},
            {'label': 'Option 2', 'value': '2'},
        ],
        value='1',
        id='dropdown-example'
    ),
    dcc.Slider(0, 10, 1, value=5, id='slider-example'),
    dcc.Graph(id='graph-example')
])

if __name__ == '__main__':
    app.run(debug=True)