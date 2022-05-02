import os

from flask import Flask, jsonify, request

#initialize Flask app
app = Flask(__name__)

#load the model from the given link
def load_model():
    with open('phish-model-1649995335.cloudpickle', 'rb') as f:
        clf_loaded = pickle.load(f)
    return clf_loaded

model = load_model()

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)



@app.route('/ping', methods=['GET'])
def ping_pong():
    '''
    Sanity check route
    '''
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
        prediction = model.predict([[length]])
        response_object['predict'] = prediction.tolist()[0][1]

    return jsonify(response_object)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
