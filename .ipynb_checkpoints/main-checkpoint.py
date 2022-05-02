import os

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# /predict route accepts JSON
@app.route('/predict', methods=['POST'])
def predict():
    '''
    This function takes in JSON as input, outputs prediction from the pickled load_model
    '''
    response_object = {'status':'success'}
    if request.method == 'POST':
        url = request.get_json()
        length = len(url)
        prediction = model.predict_proba([[length]])
        response_object['predict'] = prediction.tolist()[0][1]
    
    return jsonify(response_object)

    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))