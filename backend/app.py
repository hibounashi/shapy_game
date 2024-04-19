from flask import Flask, render_template, request, jsonify
from expert_system import forwardChainQuery, convertToKBFeatures, extractShapeNames
app = Flask(__name__)

@app.route('/backend/templates/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        data = request.json
        after_aima = extractShapeNames(forwardChainQuery(convertToKBFeatures(data)))
        print("Received data:", extractShapeNames(forwardChainQuery(convertToKBFeatures(data))))  # Print the received data
        return jsonify({'finnn': after_aima})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




