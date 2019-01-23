import dash
import dash_core_components as dcc
import dash_html_components as html

from menu import get_menu
from header import *


app = dash.Dash(__name__)
server = app.server




app.layout = html.Div([Header(), 
    
    #html.H1(children=get_menu()),

    dcc.Graph(id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'bar', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }),
    dcc.Graph(id='example2',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [3, 5, 9, 3, 4], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [6, 5, 7, 1, 9], 'type': 'line', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
