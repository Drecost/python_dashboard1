import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output
import random
import datetime




app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
server = app.server

app.layout = html.Div([
    html.Div([
            html.Div([
            html.Img(src=app.get_asset_url('estacio-logo.jpg'),
                    id = 'exclusiva-image',
                    style={'height': '75px',
                            'width': 'auto',
                            'margin-bottom': '25px',    
                            'border-radius':'3px'})
                     
        ], className='one-third column'), #LOGO 

        html.Div([
            html.Div([
                html.H2('Python com Arduíno', style={'color':'white'}),
                html.P('Obs: Dados gerados randômicamente!', style={'color':'white'}),
            ])

        ], className='one-half column', id = 'title'), # TITULO

        
            html.Div([
                html.H6('IOT E INDÚSTRIA 4.0 EM PYTHON', style={'color':'orange'}),
            ], className='one-half column', id = 'title1'),
                        

        ], id = 'header', className='row flex-display', style={'margin-bottom': '25px'}), # CABEÇALHO


    html.Div([    
        html.Div([
            html.Div([
                dcc.Graph(
                    id='grafico_luz'
                ),
                dcc.Interval(
                    id='interval-component',
                    interval=5*1000, # in milliseconds
                    n_intervals=0
                )
            ], className='card_container seven columns'),

            html.Div([
                html.P('Sensor DHT11: Temperatura ❄', style={'color':'white','fontSize':22,'margin-top':'2rem'}),
                html.Div([
                    html.H1(
                    id='indicador_temperatura',
                    style={'color':'white','fontSize':150}
                ),
                ], style={'margin-top':'9rem'}),
                dcc.Interval(
                    id='interval-component2',
                    interval=5*1000, # in milliseconds
                    n_intervals=0
                )
            ], className='card_container four columns', style={'height': '480px','textAlign':'center'}),

            html.Div([
                dcc.Graph(
                    id='grafico_vibracao'
                ),
                dcc.Interval(
                    id='interval-component3',
                    interval=5*1000, # in milliseconds
                    n_intervals=0
                )
            ], className='card_container seven columns'),

            html.Div([
                html.P('Sensor DHT11: Umidade ☂', style={'color':'white','fontSize':22,'margin-top':'2rem'}),
                html.Div([
                    html.H1(
                    id='indicador_umidade',
                    style={'color':'white','fontSize':150}
                ),
                ], style={'margin-top':'9rem'}),
                dcc.Interval(
                    id='interval-component4',
                    interval=5*1000, # in milliseconds
                    n_intervals=0
                )
            ], className='card_container four columns', style={'height': '480px','textAlign':'center'}),
        

    ], className='row flex display'),

    html.Footer([
    html.Div([
        html.Span('Desenvolvido por: ', style={'color':'white'}),
        html.A('André Costa', href='https://github.com/drecost', target="_blank")
    
    ], style={'text-align': 'center', 'margin-top': '25px'}),
    
])

], id = 'mainContainer', style={'display': 'flex', 'flex-direction': 'column'})

])

@app.callback(
    Output('grafico_luz', 'figure'),
    Input('interval-component', 'n_intervals')
)
def atualizar_grafico_luz(n):
    data = {
        'time': [],
        'nivel_luz': [],
    }

    # Collect some data
    for i in range(180):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*5)
        luz = random.randrange(0,10)

        data['nivel_luz'].append(luz)
        data['time'].append(time)
        


    fig = go.Figure()

    fig.update_layout(
        title={'text': 'Sensor LDR: Nivel de Luz ☀︎',
                    'y': 0.93,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
                   titlefont={'color': 'white',
                       'size': 20},
            font=dict(family='sans-serif',
                      color='white',
                      size=12),
            hovermode='closest',
            paper_bgcolor='#333',
            plot_bgcolor='#333',
            legend={'orientation': 'h',
                    'bgcolor': '#333',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
    ),


    fig.add_trace(go.Scatter(
        x=data['time'], 
        y=data['nivel_luz'],
        line_color='rgb(127,255,212)',
        name='Fair',
        fill='tozeroy', #fill='tozeroy',tonexty
        fillcolor='rgba(127,255,212,0.5)'
    ))
    fig.update_traces(mode='lines')
 

    return fig


@app.callback(
    Output('grafico_vibracao', 'figure'),
    Input('interval-component3', 'n_intervals')
)
def atualizar_grafico_vibracao(n):
    data = {
        'time': [],
        'nivel_vibracao': [],
    }

    # Collect some data
    for i in range(180):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*10)
        vibracao = random.randrange(500,1000)

        data['nivel_vibracao'].append(vibracao)
        data['time'].append(time)


    fig = go.Figure()

    fig.update_layout(
        title={'text': 'Sensor SW-420: Nivel de Vibração ♫','y': 0.93,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
                   titlefont={'color': 'white',
                       'size': 20},
            font=dict(family='sans-serif',
                      color='white',
                      size=12),
            hovermode='closest',
            paper_bgcolor='#333',
            plot_bgcolor='#333',
            legend={'orientation': 'h',
                    'bgcolor': '#333',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
    ),


    fig.add_trace(go.Scatter(
        x=data['time'], 
        y=data['nivel_vibracao'],
        line_color='rgb(0,191,255)',
        name='Fair',
        fill='tozeroy', #fill='tozeroy',tonexty
        fillcolor='rgba(0,191,255,0.5)',
    ))
    fig.update_traces(mode='lines')
 

    return fig


@app.callback(
    Output('indicador_temperatura', 'children'),
    Input('interval-component2', 'n_intervals')
)
def atualizar_card_temperatura(n):
    data = {
        'time': [],
        'temperatura': [],
    }

    # Collect some data
    for i in range(180):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        temperatura = random.randrange(20,30)

        temperatura = str(temperatura)+'ºC'
        data['temperatura'].append(temperatura)
        data['time'].append(time)

        return data['temperatura']




@app.callback(
    Output('indicador_umidade', 'children'),
    Input('interval-component4', 'n_intervals')
)
def atualizar_card_umidade(n):
    data = {
        'time': [],
        'umidade': [],
    }

    # Collect some data
    for i in range(180):
        time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        umidade = random.randrange(10,80)

        umidade = str(umidade)+'%'
        data['umidade'].append(umidade)
        data['time'].append(time)

        return data['umidade']



if __name__ == '__main__':
    server.run(host='0.0.0.0', debug=True)
