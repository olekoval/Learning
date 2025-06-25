from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('./data/events_17packet.csv')
# перетвореня з "широкого датафрейму на довгий"   
df_melt = pd.melt(
    df,
    id_vars=['residence_area', 'report_month'],
    value_vars=['count_before_18', 'count_amb', 'count_inpat'],
    var_name='type',
    value_name='count'
).sort_values(by='residence_area')


app.layout = html.Div([
    dcc.Dropdown(options=[
        {'label': 'січень', 'value': 1},
        {'label': 'лютий', 'value': 2},
        {'label': 'березень', 'value': 3},
        {'label': 'квітень', 'value': 4},
        {'label': 'травень', 'value': 5},
        ], value=1, id='month'),
    
    dcc.Graph(id='region_count')
    ])

@callback(
    Output('region_count', 'figure'),
    Input('month', 'value')
    )

def region_count(month):
    # фільтр по мясяцям
    # Використовуємо глобальний df_melt, але створюємо копію для фільтрації
    df_filter = df_melt[df_melt['report_month'] == month].copy()
    # остаточне групування після вибора місяців
    df_region = df_filter.groupby(['residence_area', 'type'], as_index=False)['count'].sum()
        
    fig = go.Figure(data=[
        go.Bar(
            name='Амбулаторна допомога',
            x=df_region[df_region['type'] == 'count_amb']['residence_area'],
            y=df_region[df_region['type'] == 'count_amb']['count']
        ),
        go.Bar(
            name='Стаціонарна допомога',
            x=df_region[df_region['type'] == 'count_inpat']['residence_area'],
            y=df_region[df_region['type'] == 'count_inpat']['count']
        ),
        go.Bar(
            name='Діти до 18 років',
            x=df_region[df_region['type'] == 'count_before_18']['residence_area'],
            y=df_region[df_region['type'] == 'count_before_18']['count']
        )
    ])
    fig.update_layout(barmode='stack')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
