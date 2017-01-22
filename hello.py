from flask import Flask, url_for, json
from flask import render_template
from flask import request
# from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import os
import requests
import json
# import asyncio

# from me import crossdomain
app = Flask(__name__)
api = Api(app)
# CORS(app)

def ottoCode():
    url = 'https://bldg-pi-api.ou.ad3.ucdavis.edu/piwebapi/search/query?q=afelementtemplate:Domestic%20AND%20afelementtemplate:Water%20AND%20afelementtemplate:Gal%20NOT%20afelementtemplate:Manual&fields=name;links&count=100'
    #headers = {'Content-Type': 'application/json'}

    #filters = [dict(name='name', op='like', val='%y%')]
    #params = dict(q=json.dumps(dict(filters=filters)))

    response = requests.get(url, auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))#, params=params)
    #assert response.status_code == 200
    buildings = response.json()["Items"]
    i = 0
    leng = len(buildings)
    dictionary = {}
    for building in buildings:
        try:
            print("Loading " + str(i) + " out of " + str(leng))
            i = i + 1
            response = requests.get(building["Links"]["Self"] + "?fields=name;links", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            parent = requests.get(response.json()["Links"]["Parent"] + "?fields=name;links", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            attr = requests.get(parent.json()["Links"]["Attributes"] + "?fields=name;items", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            if len(attr.json()["Items"]) > 1:
                for item in attr.json()["Items"]:
                    if item["Name"] == "Asset Number":
                        assetNo = requests.get(item["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8')).json()["Value"]
                        break
                if assetNo == "":
                    continue
                time1 = requests.get(response.json()["Links"]["Value"] + "?fields=name;items", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                for item in time1.json()["Items"]:
                    if item["Name"] == "Cumulative Use":
                        usage1 = item["Value"]["Value"]

                time2 = requests.get(response.json()["Links"]["Value"] + "?time=*-1w&fields=name;items", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                for item in time2.json()["Items"]:
                    if item["Name"] == "Cumulative Use":
                        usage2 = item["Value"]["Value"]

                time3 = requests.get(response.json()["Links"]["Value"] + "?time=*-2w&fields=name;items", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                for item in time3.json()["Items"]:
                    if item["Name"] == "Cumulative Use":
                        usage3 = item["Value"]["Value"]
                print("Asset " + str(assetNo) + " usage last week: " + str(usage2 - usage3) + ", usage this week:" + str(usage1 - usage2))
                if (usage2 - usage3 != 0):
                    print((usage1 - usage2)/(usage2 - usage3))
                    dictionary[assetNo] = (usage1 - usage2)/(usage2 - usage3)
                else:
                    if (usage1 - usage2 == 0):
                        dictionary[assetNo] = 1
                    else:
                        dictionary[assetNo] = 2
        except:
            print("MISS " + str(i-1))
            continue
    return dictionary


class locations(Resource):
    def get(self):
        dictionary = ottoCode()
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "static/", "data1.json")
        data = json.load(open(json_url))
        newData = []
        for element in data:
           if element['assetNumber'] in dictionary.keys():
              element['val'] = dictionary[element['assetNumber']]
              newData.append(element)


        # print(newData)
        return newData, 200


@app.route('/')
def perry():
    return render_template('index.html')

@app.route('/map')
# @crossdomain(origin='*')
# @cross_origin()
def hello_world():
    return render_template('feature_layer.html')


def otto():
    url = 'https://bldg-pi-api.ou.ad3.ucdavis.edu/piwebapi/search/query?q=afelementtemplate:Domestic%20AND%20afelementtemplate:Water%20AND%20afelementtemplate:Gal%20NOT%20afelementtemplate:Manual&fields=name;links&count=100'
    #headers = {'Content-Type': 'application/json'}

    #filters = [dict(name='name', op='like', val='%y%')]
    #params = dict(q=json.dumps(dict(filters=filters)))

    response = requests.get(url, auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))#, params=params)
    #assert response.status_code == 200
    buildings = response.json()["Items"]
    i = 0
    leng = len(buildings)
    dictionary = {}
    for building in buildings:
        print("Loading: " + str(i) + " out of " + str(leng))
        i = i + 1
        response = requests.get(building["Links"]["Self"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

        parent = requests.get(response.json()["Links"]["Parent"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
        attr = requests.get(parent.json()["Links"]["Attributes"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
        if len(attr.json()["Items"]) > 1:
            for item in attr.json()["Items"]:
                if item["Name"] == "Asset Number":
                    assetNo = requests.get(item["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8')).json()["Value"]
                    break
            if assetNo == "":
                continue
            time1 = requests.get(response.json()["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            for item in time1.json()["Items"]:
                if item["Name"] == "Cumulative Use":
                    usage1 = item["Value"]["Value"]

            time2 = requests.get(response.json()["Links"]["Value"] + "?time=*-1w", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            for item in time2.json()["Items"]:
                if item["Name"] == "Cumulative Use":
                    usage2 = item["Value"]["Value"]

            time3 = requests.get(response.json()["Links"]["Value"] + "?time=*-2w", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            for item in time3.json()["Items"]:
                if item["Name"] == "Cumulative Use":
                    usage3 = item["Value"]["Value"]
            print("Usage 1: "+ str(usage1) + ", Usage 2: " + str(usage2) + ", Usage 3: " + str(usage3))
            if (usage2 - usage3 != 0):
                print("Usage Ratio: " + str((usage1 - usage2)/(usage2 - usage3)))
                dictionary[assetNo] = (usage1 - usage2)/(usage2 - usage3)
            else:
                if (usage1 - usage2 == 0):
                    dictionary[assetNo] = 1
                else:
                    dictionary[assetNo] = 2
    return dictionary

api.add_resource(locations, '/locations')

if __name__ == "__main__":
    app.run()