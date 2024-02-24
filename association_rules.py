from apyori import apriori as ap   

from flask import Blueprint,render_template,request,jsonify
from werkzeug.utils import secure_filename
import pandas as pd      
import numpy as np         

association_rules = Blueprint('association_rules', __name__)
ALLOWED_EXTENSIONS = set(['csv'])

@association_rules.route('/', methods=['POST'])
def index():

    #Importamos los datos
    ra_file = request.files["csvfile"]

    # Obtenemos el nombre del archivo
    filename = secure_filename(ra_file.filename)

    # Separamos el nombre del archivo
    file = filename.split('.')
    
    if file[1] in ALLOWED_EXTENSIONS:
        #     # Leemos los datos
        df = pd.read_csv(ra_file,on_bad_lines='skip')

        df_first_10 = df.head(10)

        # Converting to html Table
        table_preview = df_first_10.to_html()

        data = {
            'status': 200,
            'message': filename, 
            "preview": table_preview
        }
  
        return jsonify(data)

        # #Se incluyen todas las transacciones en una sola lista
        # transacciones = df.values.reshape(-1).tolist() #-1 significa 'dimensión desconocida'
        
        # #Se crea una matriz (dataframe) usando la lista y se incluye una columna 'Frecuencia'
        # lista = pd.DataFrame(transacciones)
        # lista['Frecuencia'] = 1

        # #Se agrupa los elementos
        # lista = lista.groupby(by=[0], as_index=False).count().sort_values(by=['Frecuencia'], ascending=True) #Conteo
        # lista['Porcentaje'] = (lista['Frecuencia'] / lista['Frecuencia'].sum()) #Porcentaje
        # lista = lista.rename(columns={0 : 'Item'})
        

        # #Se crea una lista de listas a partir del dataframe y se remueven los 'NaN'
        # #level=0 especifica desde el primer índice
        # transaccionesLista = df.stack().groupby(level=0).apply(list).tolist()

        # soporte = 54/100
        # confianza = 20/100
        # elevacion = 1

        # # soporte = request.form['soporte']
        # # confianza = request.form['confianza']
        # # elevacion = request.form['elevacion']

        # reglas = ap(transaccionesLista,
        #         min_support = float(soporte)/100,
        #         min_confidence = float(confianza)/100,
        #         min_lift = float(elevacion))


        # resultados = list(reglas)
        
        # data = {
        #     'status': 200,
        #     'filename': filename, 
        #     'resultados': resultados, 
        #     'soporte': soporte, 
        #     'confianza': confianza,
        #     "elevacion": elevacion,
        #     "size": len(resultados)
        # }
  
        # return jsonify(data)

    return jsonify({"status": "200" })
