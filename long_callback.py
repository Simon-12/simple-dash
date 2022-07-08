import dash
from dash.dependencies import Output, Input
import time


def register_long_callback(app):
    @app.long_callback(
        [Output('store-results', 'data'),
         Output('alert-finished', 'is_open')],
        inputs=[Input('button-start', 'n_clicks')],
        running=[(Output('button-start', 'disabled'), True, False),
                 (Output('button-cancel', 'disabled'), False, True)],
        cancel=[Input('button-cancel', 'n_clicks')],
        progress=[Output('progress', 'value'),
                  Output('progress', 'label')],
        prevent_initial_call=True
    )
    def start_processing(set_progress, n_clicks):

        if n_clicks is None:
            return dash.no_update

        for i in range(101):
            print(i)
            set_progress((i, f'{i}%'))
            time.sleep(0.3)

        return '', True
