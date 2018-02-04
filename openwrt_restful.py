from flask import Flask, request
from flask_restplus import Resource, Api

from cl_api import *

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# ss runnig status
@api.route('/ss/status')
class ShadowSocks(Resource):
    def get(self):
        return {"status": 'STOP' if run_cmd(cl_dict['ss']['status']) == '0' else 'RUNNING'}

    def put(self):
        cmd = cl_dict['ss'][request.form['status']]
        run_cmd(cmd)
        return "run %s success" % cmd



# ss config
@api.route('/ss/conf')
class ShadowSocksConf(Resource):
    def get(self):
        pass

    def post(self):
        pass


# ss gfw list
@api.route('/ss/gfw')
class ShadowSocksGfw(Resource):
    def get(self):
        return read_gfwlist()

    def post(self):
        url = request.form['url']
        add_gfwlist(url)
        return 'Add %s success' % url


if __name__ == '__main__':
    app.run(debug=True)
