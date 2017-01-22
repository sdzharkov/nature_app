from flask import Flask, url_for, json
from flask import render_template
from flask import request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import os

# from me import crossdomain
app = Flask(__name__)
api = Api(app)
# CORS(app)

class locations(Resource):
    def get(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "static/", "build.json")
        data = json.load(open(json_url))
        return data, 200

@app.route('/')
# @crossdomain(origin='*')
# @cross_origin()
def hello_world():
    return render_template('feature_layer.html')


@app.route('/vis')
def show():
    return render_template('visualization.html')


api.add_resource(locations, '/locations')

if __name__ == "__main__":
    app.run()