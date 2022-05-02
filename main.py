import os
import cloudpickle
import datetime
from flask import Flask, jsonify, request, json
from werkzeug.exceptions import HTTPException
import logging # <-- added


#initialize Flask app
app = Flask(__name__)

#load the model from the given link
def load_model():
    with open('phish-model-1649995335.cloudpickle', 'rb') as f:
        clf_loaded = cloudpickle.load(f)
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


@app.route('/predict', methods=['POST'])
def predict():
    '''
    This function takes in a LIST of urls as input, outputs prediction from the pickled load_model
    '''
    timestamp = datetime.datetime.now()
    response_object = {'status':'success', 'timestamp':str(timestamp), 'predictions':[]}
    if request.method == 'POST':
        data = request.get_json()
        urls = data['domain'] #the key for POSTed jsons with values of our URLS to parse should be 'domain'
        # at this point, we have a list of urls to parse, the response object requires a prediction for each url provided.
        iterator = 0
        for url in urls:
            pred = model.predict(url)
            response_object['predictions'][iterator] = pred.tolist()[0][1]
            iterator += 1
        #response_object['predict'] = prediction.tolist()[0][1]

    return jsonify(response_object)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
