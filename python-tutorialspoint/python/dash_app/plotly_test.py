import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

import plotly.express as px
import plotly.graph_objects as graph_objects


gapminder = px.data.gapminder()
gapminder.head()

scatter_fig = px.scatter(data_frame=gapminder,
           x='gdpPercap',
           y='lifeExp',
           size='pop',
           facet_col='continent',
           color='continent',
           title='Life Expectancy and GPD per capita from 1952 to 2007',
           labels={'gdpPercap': 'GDP per Capita','lifeExp': 'Life Expectancy'},
           log_x=True,
           range_y=[20,100],
           hover_name='country',
           size_max=80,
           animation_frame='year'         
           )    

#try facet_row as well          
#check scatter documentation
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

country = gapminder['country'].unique()
year = gapminder['year'].unique()

app.layout = dbc.Container([
    html.H2("Gapminder Dashboard", className="text-center my-4"),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='country_dropdown',
                options=[{'label': c, 'value': c} for c in country],
                placeholder='Select a country',
                clearable=True
            ),
        ], width=6),
        dbc.Col([
            dcc.Dropdown(
                id='year_dropdown',
                value=2007,
                options=[{'label': c, 'value': c} for c in year],
                placeholder='Select a year',
                clearable=True
            ),
        ], width=6),
    ]),
    html.Br(),
    html.Div(id='country_output'),
    dbc.Row([
        dbc.Col(dcc.Graph(id='pop_by_year'), md=6),
        dbc.Col(dcc.Graph(id='lifeexp_by_year'), md=6),
        dbc.Col(dcc.Graph(id='country_trend')), 
        dcc.Graph(id='scatter_plot', figure=scatter_fig)       
    ]),
], fluid=True)

@app.callback(Output('country_output', 'children'),
              Input('country_dropdown', 'value'),
              Input('year_dropdown', 'value'))
def display_country(country, year):
    if not country:
        return ''
    gapminder_filtered = gapminder[(gapminder['country']==country)    
    & (gapminder['year']==year)]   #filtered data frame
    le = gapminder_filtered.loc[:, 'lifeExp'].values[0]
    pop = gapminder_filtered.loc[:, 'pop'].values[0]
    return [
        html.H3(country),
        html.P(f'''In {country} the life expectancy in {year} was {le} 
        and the population was {pop:}''')  #passed -the list- into the childeren parameter of the Div component 
    ]
@app.callback(Output('pop_by_year', 'figure'),
             Input('year_dropdown', 'value')
)
def pop_by_year(year):
    gapminder_year = gapminder[gapminder['year']==year]
    gapminder_year = gapminder_year[['country', 'pop']]
    gapminder_year = gapminder_year.sort_values(by='pop', ascending=False)[:10]   #select all rows up and untill the tenth item. 
    fig = graph_objects.Figure()
    fig.add_bar(x=gapminder_year['country'], y=gapminder_year['pop'])
    fig.layout.title = f'Top ten countries by population - {year}'
    return fig

@app.callback(Output('lifeexp_by_year', 'figure'),
             Input('year_dropdown', 'value')
)
def lifeexp_by_year(year):
    gapminder_year = gapminder[gapminder['year']==year]
    gapminder_year = gapminder_year[['country', 'lifeExp']]
    gapminder_year = gapminder_year.sort_values(by='lifeExp', ascending=False)[:10]   #select all rows up and untill the tenth item. 
    fig = graph_objects.Figure()
    fig.add_bar(x=gapminder_year['country'], y=gapminder_year['lifeExp'])
    fig.layout.title = f'Top ten countries by life expectation - {year}'
    return fig

@app.callback(
    Output('country_trend', 'figure'),
    Input('country_dropdown', 'value')
)
def country_trend(country):
    if not country:
        return graph_objects.Figure()
    df = gapminder[gapminder['country'] == country]
    fig = px.line(df, x='year', y='lifeExp', title=f'Life Expectancy over Time - {country}')
    return fig

if __name__ == '__main__':
    app.run(debug=True, port=8192)

# try to add chart with the top 10 countries showing the highest life expectancy. 