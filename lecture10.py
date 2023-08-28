from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)
server = app.server

app.title = "MCM7003 Data Visualization Interactive Demo" 

fig1 = px.line(x=["a","b","c","d","e"], y=[1,3,2,2,3], title="Figure 1: Line Chart")	

df = px.data.iris()
fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Figure 2: Scatter Plot")

app.layout = html.Div(
    [html.H1("Data Visualization"),
    dcc.RadioItems(id='my-radio', options=['Figure 1', 'Figure 2'], value='Figure 1', inline=True),
    dcc.Graph(id='graph-output', figure ={})]
)


@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    Input(component_id='my-radio', component_property='value')
)

def update_my_graph(val_chosen):
    if (val_chosen == 'Figure 1'):
        return fig1	
    else:
        return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
