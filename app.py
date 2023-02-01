import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import DiskcacheManager
from flask import Flask
from long_callback import register_long_callback
import diskcache


# DiskCache
cache = diskcache.Cache('./cache')
long_callback_manager = DiskcacheManager(cache)

# Create app
server = Flask(__name__)
app = dash.Dash(server=server, background_callback_manager=long_callback_manager)
app.title = 'My App'
server = app.server
register_long_callback(app)


app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(
            html.Div([

                # Start
                dbc.Button('Start Processing', id='button-start', color='info',
                           style={'font-weight': 'bold',
                                  'margin-top': '24px',
                                  'margin-bottom': '24px'}),

                # Progress and cancel
                html.Div([
                    dbc.Progress(id='progress', animated=True, striped=True, value=0, max=100,
                                 label='0%', color='success',
                                 style={'height': '30px',
                                        'font-weight': 'bold',
                                        'margin-bottom': '24px'}),
                    dbc.Button('Cancel', id='button-cancel', color='danger', disabled=True,
                               style={'font-weight': 'bold'})
                ], className='d-grid'),

                # Alert
                dbc.Row(
                    dbc.Col(
                        dbc.Alert('Finished successfully!', id='alert-finished',
                                  dismissable=True, is_open=False, fade=True,
                                  style={'margin-top': '24px'})
                    )
                ),

            ], className='d-grid'),
            width=11, align='center'), justify='center'
    ),

    # Store
    dcc.Store(id='store-results')


], fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True)
