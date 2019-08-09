import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import json

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/737dc4ab11f7a1a8d6b5645d26f69133d97062ae/dash-wind-streaming.css",
                "https://fonts.googleapis.com/css?family=Raleway:400,400i,700,700i",
                "https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i",
                "https://fonts.googleapis.com/css?family=Roboto:300,400,500"
                "https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700"]

external_stylesheets=external_css

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Div([
        html.H2("Currency converter"),
        html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe-inverted.png"),
		
		
	], className='banner'),
    html.Hr(),
    html.Div([
        html.Label("Amount: "),
        dcc.Input(id = 'amount',
                  type='text',
                  value=100
        
    ), 
		
		
	],style={'display': 'inline-block','width': '30%'}),
    
    html.Hr(),
    html.Div([html.Div([
                html.Label("Currency: "),
                dcc.Dropdown(id = 'curr1',
                    options=[
                            {'label': 'GBP', 'value': 'GBP'},
                            {'label': 'HKD', 'value': 'HKD'},
                            {'label': 'IDR', 'value': 'IDR'},
                            {'label': 'ILS', 'value': 'ILS'},
                            {'label': 'DKK', 'value': 'DKK'},
                            {'label': 'INR', 'value': 'INR'},
                            {'label': 'CHF', 'value': 'CHF'},
                            {'label': 'MXN', 'value': 'MXN'},
                            {'label': 'CZK', 'value': 'CZK'},
                            {'label': 'SGD', 'value': 'SGD'},
                            {'label': 'THB', 'value': 'THB'},
                            {'label': 'HRK', 'value': 'HRK'},
                            {'label': 'EUR', 'value': 'EUR'},
                            {'label': 'MYR', 'value': 'MYR'},
                            {'label': 'NOK', 'value': 'NOK'},
                            {'label': 'CNY', 'value': 'CNY'},
                            {'label': 'BGN', 'value': 'BGN'},
                            {'label': 'PHP', 'value': 'PHP'},
                            {'label': 'PLN', 'value': 'PLN'},
                            {'label': 'ZAR', 'value': 'ZAR'},
                            {'label': 'CAD', 'value': 'CAD'},
                            {'label': 'ISK', 'value': 'ISK'},
                            {'label': 'BRI', 'value': 'BRI'},
                            {'label': 'RON', 'value': 'RON'},
                            {'label': 'NZD', 'value': 'NZD'},
                            {'label': 'TRY', 'value': 'TRY'},
                            {'label': 'JPY', 'value': 'JPY'},
                            {'label': 'RUB', 'value': 'RUB'},
                            {'label': 'KRW', 'value': 'KRW'},
                            {'label': 'USD', 'value': 'USD'},
                            {'label': 'AUD', 'value': 'AUD'},
                            {'label': 'HUF', 'value': 'HUF'},
                            {'label': 'SEK', 'value': 'SEK'},
                            
                    ],
                    value='USD'
                ),
               
                
                
            ],style={'display': 'inline-block','width': '15%'}),
            
            html.Div([
                html.Label("Output currency: "),
                dcc.Dropdown(id = 'curr2',
                    options=[
                        {'label': 'GBP', 'value': 'GBP'},
                            {'label': 'HKD', 'value': 'HKD'},
                            {'label': 'IDR', 'value': 'IDR'},
                            {'label': 'ILS', 'value': 'ILS'},
                            {'label': 'DKK', 'value': 'DKK'},
                            {'label': 'INR', 'value': 'INR'},
                            {'label': 'CHF', 'value': 'CHF'},
                            {'label': 'MXN', 'value': 'MXN'},
                            {'label': 'CZK', 'value': 'CZK'},
                            {'label': 'SGD', 'value': 'SGD'},
                            {'label': 'THB', 'value': 'THB'},
                            {'label': 'HRK', 'value': 'HRK'},
                            {'label': 'EUR', 'value': 'EUR'},
                            {'label': 'MYR', 'value': 'MYR'},
                            {'label': 'NOK', 'value': 'NOK'},
                            {'label': 'CNY', 'value': 'CNY'},
                            {'label': 'BGN', 'value': 'BGN'},
                            {'label': 'PHP', 'value': 'PHP'},
                            {'label': 'PLN', 'value': 'PLN'},
                            {'label': 'ZAR', 'value': 'ZAR'},
                            {'label': 'CAD', 'value': 'CAD'},
                            {'label': 'ISK', 'value': 'ISK'},
                            {'label': 'BRI', 'value': 'BRI'},
                            {'label': 'RON', 'value': 'RON'},
                            {'label': 'NZD', 'value': 'NZD'},
                            {'label': 'TRY', 'value': 'TRY'},
                            {'label': 'JPY', 'value': 'JPY'},
                            {'label': 'RUB', 'value': 'RUB'},
                            {'label': 'KRW', 'value': 'KRW'},
                            {'label': 'USD', 'value': 'USD'},
                            {'label': 'AUD', 'value': 'AUD'},
                            {'label': 'HUF', 'value': 'HUF'},
                            {'label': 'SEK', 'value': 'SEK'},
                    ],
                    value='CZK'),
                
               
                
                
            ],style={'display': 'inline-block','width': '15%'})]),
    
    
    html.Hr(),
    html.Br(),
    
    html.Label("Output amount: "),
    html.Div(id='final_dict'),
    
    

    ])

from forex_python.converter import CurrencyRates
c = CurrencyRates()

@app.callback(Output('final_dict','children'),
			 [Input('amount','value'),
			  Input('curr1','value'),
			  Input('curr2','value')])
def convert(amount,curr1,curr2):
    a=float(amount)
    if curr2:
        res = c.get_rates(curr1) 
        for i in res:
            res[i]=res[i]*a

        res_filt = {k: v for k, v in res.items() if k.startswith('{}'.format(curr2))}
        result = dict(input=dict(amount=a,
                                 currency=curr1),
                     output=dict(res_filt))
    else:
        res = c.get_rates(curr1)  
        for i in res:
            res[i]=res[i]*a

        result = dict(input=dict(amount=a,
                                 currency=curr1),
                     output=dict(res))
	 
	

    return json.dumps(result)


if __name__ == '__main__':
    app.run_server(debug=True, port = 8000)
