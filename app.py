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



app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
        html.H2("Stock App"),
        html.Img(src="./assets/stock-icon.png")
    ],className="banner"),


    html.H1(children="Hello World"),
    html.Label("Dash Graphs"),
    #html.Div(
        dcc.Graph(id="Stock Chart",figure=fig)
    #)


    ])


app.css.append_css({
    "external_url":"https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == "__main__":
    app.run_server(debug=True)
