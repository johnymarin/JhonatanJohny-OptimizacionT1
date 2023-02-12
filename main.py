# This is a sample Python script.
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.express as px
import numpy as np
from dash.dependencies import Input, Output
from flask import Flask
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


server = Flask(__name__)
app = dash.Dash(server=server)

# Define la función a evaluar
def func(x):
    return x**2 - 4

# Define la solución encontrada por el método de bisección
x_lower = 1
x_upper = 2
epsilon = 0.01
x_middle = (x_lower + x_upper) / 2
y_middle = func(x_middle)

# Genera los datos para la gráfica
x_vals = np.linspace(x_lower, x_upper, 100)
y_vals = func(x_vals)

# Crea la gráfica
fig = px.line(x=x_vals, y=y_vals, title="Método de Bisección")
fig.add_scatter(x=[x_middle], y=[y_middle], mode='markers', marker=dict(size=10, color='red'))

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)