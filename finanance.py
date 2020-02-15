import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from iexfinance.stocks import Stock

aapl = Stock("AAPL",token="pk_c3191cfc5df94580bb6f01a4414c6f9d",output_format='pandas')
df = aapl.get_historical_prices()


traceClose = go.Scatter(x=list(df.index),
           y=list(df.close),
           name="Close",
           line=dict(color="#f44242")
           )

data = [traceClose]

layout = dict(title='Stock Chart')

fig = dict(data=data,layout=layout)



app = dash.Dash()

app.layout = html.Div([
    html.H1(children="Hello World"),
    html.Label("Dash Graphs"),
    html.Div(
        dcc.Graph(id="Stock Chart",figure=fig)
    )


    ])

if __name__ == "__main__":
    app.run_server(debug=True)
