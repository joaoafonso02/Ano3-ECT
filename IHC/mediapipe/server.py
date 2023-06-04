from flask import Flask, jsonify, request
from flask_cors import CORS

import mediapipe_solutions


app = Flask(__name__)
CORS(app)

# Example route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Example API endpoint
@app.route('/api/example', methods=['GET'])
def get_example():
    data = {
        'message': 'This is an example API endpoint',
        'status': 'success'
    }
    return jsonify(data)

# Example API endpoint with query parameters
@app.route('/api/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name')
    if name:
        message = f'Hello, {name}!'
    else:
        message = 'Hello, there!'
    data = {
        'message': message,
        'status': 'success'
    }
    return jsonify(data)

@app.route('/api/feature')
def api_feature():
    return mediapipe_solutions.available

@app.route('/api/feature/<feature_name>', methods=['POST'])
def api_feature_name(feature_name):
    if feature_name not in mediapipe_solutions.available:
        return {"status": "invalid feature"}

    func = getattr(mediapipe_solutions, feature_name)
    result = func(request.files['blob'])

    return result

if __name__ == '__main__':
    app.run(debug=True)