from tornado import web, ioloop
import json
import numpy as np


class IndexHandler(web.RequestHandler):
    def get(self):
        self.write(json.dumps({'status': 'ok - tornado'}))


class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def post(self, *args):
        print('received')
        # # finish this response
        # self.finish()

        # regress
        data = json.loads(self.request.body.decode('utf-8'))
        Y = np.asarray(data['Y_train'])
        X = np.asarray(data['X_train'])
        X_test = np.asarray(data['X_test'])
        X = np.insert(X, 0, 1.0, axis=1)
        X_test = np.insert(X_test, 0, 1.0, axis=1)
        W = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
        Y_hat = list(np.dot(X_test, W).flatten())

        self.write(json.dumps({'Y_hat':Y_hat}))

        # # finish this response
        self.finish()

app = web.Application([
    (r'/', IndexHandler),
    (r'/regress', ApiHandler)
])

if __name__ == '__main__':
    print('server listening on port 80')
    app.listen(80)
    ioloop.IOLoop.instance().start()
