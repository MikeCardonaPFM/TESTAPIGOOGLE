import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from decouple import config



#Librerias para el manejo de la API de AppSheet por Mike
##################################################################################
API_KEY = config('API_KEY')

##################################################################################
class BotMike():
    def __init__(self, APP_ID, API_KEY, table, data):
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.data = data
        self.API_URL = f"https://www.appsheet.com/api/v2/apps/{self.APP_ID}/tables/{table}/"
        
        self.headers = {
            "ApplicationAccessKey": self.API_KEY
        }

    def post_table(self):
        action = "Action"
        url = self.API_URL + action
        response = requests.post(url, json=self.data, headers=self.headers)
        return response.json()
    
    def get_table(self):
        action = "find"
        url = self.API_URL + action
        response = requests.post(url, json=self.data, headers=self.headers)


        if response.status_code == 200:
            #Uso de pandas para la lectura de la tabla
            df = pd.DataFrame(response.json())

            get_df_limpio = self.limpieza_datos(df)
            gte_graficos_chidos_show = self.get_graficos_chidos(get_df_limpio)

            return df
        else:
            return f"Error {response.status_code}: {response.text}"
        

    def limpieza_datos(self, df_sucio):
        "Un ejemlo de como ir limpiando los datos de ser necesario"
        df_sucio["FECHA_SOLICITUD_CLIENTE"] = pd.to_datetime(df_sucio["FECHA_SOLICITUD_CLIENTE"], errors='coerce')
        df_sucio = df_sucio.drop(["_RowNumber", "Row ID"], axis=1)
        
        # Reemplazar valores vacíos en "ESTATUS" por "Desconocido"
        df_sucio["ESTATUS"].fillna("Desconocido", inplace=True)
        df_limpio = df_sucio
        return df_limpio

    def get_graficos_chidos(self, df_limpionew):
        "Un ejemplo de como obtener gráficos chidos"
        

        # Gráfico de barras de la cantidad de solicitudes por estatus
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df_limpionew, x="ESTATUS")
        plt.title("Cantidad de solicitudes por estatus")
        plt.xticks(rotation=45)
        plt.show()
        
        # Gráfico de barras de la cantidad de solicitudes por tipo
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df_limpionew, x="Type")
        plt.title("Cantidad de solicitudes por tipo")
        plt.xticks(rotation=45)
        plt.show()
        




        

mike = BotMike(config('APP_ID'), API_KEY, "WO", {"Action": "find"})
print(mike.get_table())

##########################################################################################