from flask import Flask, jsonify, request
from flask_cors import CORS

from pcbPrediction import predict_pcb

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload_file():
    print("Upload file called")
    # json_string = request.json
    # print(json_string)
    if 'file' not in request.files:
        print("No file part")
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        print("No selected file")
        return jsonify({'error': 'No selected file'})
    else:
        print(file.filename)
        prediction = predict_pcb(file)
        print("Prediction:", prediction)
        response_json = {'pcbFault': prediction}

    return jsonify(response_json)


if __name__ == '__main__':
    app.run(debug=True)
