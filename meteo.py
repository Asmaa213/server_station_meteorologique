from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId  # Importer ObjectId pour pouvoir l'exclure lors de la sérialisation JSON

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['station_meteorologique']
collection = db['details_of the day']

@app.route('/', methods=['GET'])
def get_all_data():
    # Exclure les identifiants ObjectId des résultats
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
