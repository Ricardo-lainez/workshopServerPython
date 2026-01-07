from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
import json

# Cargar variables de entorno
load_dotenv()

# Inicializar Flask
app = Flask(__name__, static_folder='static')
CORS(app)

# Configuración de MongoDB desde variables de entorno
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

# Validar que las variables estén configuradas
if not MONGO_URI or not DATABASE_NAME or not COLLECTION_NAME:
    raise ValueError("Error: Las variables MONGO_URI, DATABASE_NAME y COLLECTION_NAME deben estar configuradas en el archivo .env")

# Conectar a MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    print("✓ Conexión exitosa a MongoDB")
except Exception as e:
    print(f"✗ Error al conectar a MongoDB: {e}")

# Convertir ObjectId a string para JSON
def serialize_doc(doc):
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

# Ruta principal - Renderizar página HTML
@app.route('/')
def index():
    return render_template('index.html')

# API: Obtener todos los registros
@app.route('/api/customers', methods=['GET'])
def get_customers():
    try:
        customers = list(collection.find())
        customers = [serialize_doc(customer) for customer in customers]
        return jsonify({
            'success': True,
            'data': customers,
            'count': len(customers)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Configuración de Flask desde variables de entorno
    debug_mode = os.getenv('FLASK_DEBUG', 'True') == 'True'
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    app.run(debug=debug_mode, host=host, port=port)
