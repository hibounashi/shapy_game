from flask import Flask, jsonify, request
from expert_system import forwardChainQuery, convertToKBFeatures
app = Flask(__name__)

@app.route('/send', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify(forwardChainQuery(convertToKBFeatures(data)))

if __name__ == '__main__':
    app.run(debug=True)
