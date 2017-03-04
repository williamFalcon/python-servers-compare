from flask import Flask, Response, request
import json
import numpy as np

app = Flask(__name__)

@app.route("/")
def status():
    data = {'status': 'ok - uwsgi'}
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/regress', methods=['POST'])
def hello():

    data = request.get_json()
    Y = np.asarray(data['Y_train'])
    X = np.asarray(data['X_train'])
    X_test = np.asarray(data['X_test'])
    X = np.insert(X, 0, 1.0, axis=1)
    X_test = np.insert(X_test, 0, 1.0, axis=1)
    W = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
    Y_hat = list(np.dot(X_test, W).flatten())

    resp = Response(json.dumps({'Y_hat':Y_hat}), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
