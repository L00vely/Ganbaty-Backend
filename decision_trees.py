from flask import Blueprint,render_template,request,jsonify
import os
import base64
import matplotlib
matplotlib.use('Agg')
from io import BytesIO
import base64
from werkzeug.utils import secure_filename 
import pandas as pd      
import numpy as np         
import matplotlib.pyplot as plt  
import seaborn as sns     
from datetime import datetime

from utils.delete_date_columns import delete_date_columns

decision_trees = Blueprint('decision_trees', __name__)
ALLOWED_EXTENSIONS = set(['csv'])

@decision_trees.route('/', methods=['POST'])
def index():
    try:
        # Importamos los datos
        ra_file = request.files["csvfile"]

        # Obtenemos el nombre del archivo
        filename = secure_filename(ra_file.filename)

        # Separamos el nombre del archivo
        file = filename.split('.')
        
        if file[1] in ALLOWED_EXTENSIONS:
            # Leemos los datos
            df = pd.read_csv(ra_file, on_bad_lines='skip')

            # Eliminando las columnas con fechas
            df = delete_date_columns(df)

            # Mostramos los primeros 10 datos del dataframe
            df_first_10 = df.head(10)

            # Converting to html Table
            table_preview = df_first_10.to_html()

            img = BytesIO()
            correlation_dataframe = df.corr(method='pearson')
            plt.figure(figsize=(10,10))
            inference_matrix = np.triu(correlation_dataframe)
            sns.heatmap(correlation_dataframe, cmap='RdBu_r', annot=True, mask=inference_matrix)

            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            heat_map_url = base64.b64encode(img.getvalue()).decode('utf8')

            # Obtenemos el nombre de las columnas del dataframe para la selección manual
            columns_names = df.columns.values

            data = {
                'status': "loaded",
                'error': "none",
                "response": {
                    'filename': filename, 
                    "decision_tree_response": {
                        'columns_names_list': list(columns_names)
                    },
                    "preview": table_preview,
                    'heat_map_url': heat_map_url
                }
            }
    
            return jsonify(data)
        else:
            raise Exception("El formato de archivo no es válido. Solo se permiten archivos CSV.")
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})
