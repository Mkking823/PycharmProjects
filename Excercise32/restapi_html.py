from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)

# Sample data for demonstration
data = [
{"id": 1, "name": "mahesh"},
{"id": 2, "name": "aruna"},
{"id": 3, "name": "mani"},
]

#get methode
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data)

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)
