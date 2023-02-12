# This is a sample Python script.
import dash
import dash_bootstrap_components as dbc
from dash import dcc, dash_table
from dash import html
import plotly.express as px
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from flask import Flask
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


server = Flask(__name__)
app = dash.Dash(server=server)

def bisection(func, x_lower, x_upper, epsilon):
    res = []
    while abs(x_upper - x_lower) > epsilon:
        x_middle = (x_upper + x_lower) / 2
        y_middle = func(x_middle)
        res.append([x_lower, x_upper, x_middle, y_middle])
        if y_middle == 0:
            return x_middle
        elif y_middle * func(x_lower) < 0:
            x_upper = x_middle
        else:
            x_lower = x_middle
    res.append([x_lower, x_upper, (x_upper + x_lower) / 2, func((x_upper + x_lower) / 2)])
    return res

def func(x):
    return x**2 - 4

results = bisection(func, 1, 2, 0.01)

app.layout = html.Div([
    html.H1("Metodo de Bisecccion Jhonatan Restrepo - Johny Marin"),
    html.Div([
        html.Label("x_lower: x inferior"),
        dcc.Input(id="input_x_lower", value=1, type="number"),
    ]),
    html.Div([
       html.Label("x_upper: x superior"),
       dcc.Input(id="input_x_upper", value=2, type="number"),
    ]),
    html.Div([
       html.Label("epsilon: error"),
       dcc.Input(id="input_epsilon", value=0.01, type="number"),
    ]),
    html.Div([
       html.Label("Funcion: la funcion a optimizar"),
       dcc.Input(id="input_func", value="x**2 - 4", type="text"),
    ]),
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in ["x_lower", "x_upper", "x_middle", "y_middle"]],
    data=pd.DataFrame(results, columns=["x_lower", "x_upper", "x_middle", "y_middle"]).to_dict("rows"),
    ),
])

"""
@app.callback(
    dash.dependencies.Output('table', 'data'),
    [
        dash.dependencies.Input('input_x_lower', 'value'),
        dash.dependencies.Input('input_x_upper', 'value'),
        dash.dependencies.Input('input_epsilon', 'value'),
        dash.dependencies.Input('input_func', 'value')
    ]
)
def update_table(x_lower, x_upper, epsilon, func_str):
    func = eval(f"lambda x: {func_str}")
    res = bisection(func, x_lower, x_upper, epsilon)
    return res
"""

if __name__ == '__main__':
    app.run_server(debug=True)