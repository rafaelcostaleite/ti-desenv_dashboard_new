import os
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import cx_Oracle

debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True

###

#Configurações de conexão
DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'

#Pegando as credenciais via variável de ambiente

USERNAME = 'dba_egk' #os.getenv('DB_USER')
PASSWORD = 'dba_egk' #os.getenv('DB_PASSWORD')
HOST = '10.3.0.105' #os.getenv('DB_HOST')
PORT = '1245' #os.getenv('DB_PORT')
SERVICE = 'jaspe' #os.getenv('DB_SERVICE')

#Criando a string de conexão
connstr = f"{USERNAME}/{PASSWORD}@{HOST}:{PORT}/{SERVICE}"

#Conectando ao SGBD
conn = cx_Oracle.connect(connstr)

#Criando um cursor
#cursor = conn.cursor()

#Rodando uma Query para teste
#cursor.execute("select * from sch_ods.ti_incidentes_historico")
#result = cursor.fetchall()
#for row in result:
#    print('Resultado do select')
#    print(result)

df1 = pd.read_sql("select * from sch_ods.ti_incidentes_historico", con=conn)

###

app = Dash(__name__)

server = app.server

#data = pd.DataFrame(
#    {
#        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#        "Amount": [4, 1, 3, 2, 4, 5],
#        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
#    }
#)
#
#graph = px.bar(data, x="Fruit", y="Amount", color="City", barmode="group")

df = px.data.stocks()
graph = px.line(df1, x="data", y=df.columns,
              hover_data={"date": "|%B %d, %Y"},
              title='Histórico de incidentes')

app.layout = html.Div(
    children=[
        html.H1(
            children=f"Dashboard TI {'Dev Server' if debug else 'Prod Server 4'}"
        ),
        html.Div(children="""Dash: A web application framework for your data."""),
        dcc.Graph(id="example-graph", figure=graph),
    ]
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8050", debug=debug)
