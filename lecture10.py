from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px


app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Interactive Demo" 

df = pd.read_csv('https://raw.githubusercontent.com/wenjiun/MCM7003CallbackDemo/main/cpi_headline.csv')

#fig1 = px.line(x=["a","b","c","d","e"], y=[1,3,2,2,3], title="Figure 1: Line Chart")	

#fig1 = px.line(df, x='date', y=['overall', 'food_beverage', 'alcohol_tobacco',
       'clothing_footwear', 'housing_utilities', 'furnishings', 'health',
       'transport', 'communication', 'recreation_culture', 'education',
       'hospitality', 'misc'], title='Figure 1: Consumer Price Index').update_layout(xaxis_title="Date", yaxis_title="Index")

#df = px.data.iris()
#fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Figure 2: Scatter Plot")


app.layout = html.Div(
    [html.H1("Data Visualization"),
#   dcc.RadioItems(id='my-radio', options=['Figure 1', 'Figure 2'], value='Figure 1', inline=True),
    dcc.Dropdown(['overall', 'food_beverage', 'alcohol_tobacco',
       'clothing_footwear', 'housing_utilities', 'furnishings', 'health',
       'transport', 'communication', 'recreation_culture', 'education',
       'hospitality', 'misc'], 'overall', id='my-dropdown'),
    dcc.Graph(id='graph-output', figure ={})]
)


@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Input(component_id='my-dropdown', component_property='value')
)
def update_my_graph(val_chosen):
    fig1 = px.line(df, x='date', y=val_chosen, title=val_chosen).update_layout(xaxis_title="Date", yaxis_title="Index")
    return fig1	



if __name__ == '__main__':
    app.run_server(debug=True)
