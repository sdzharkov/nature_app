from flask import Flask, url_for, json
from flask import render_template
from flask import request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import os
import requests
import json
import asyncio

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
    j = 0
    dictionary = {}
    for building in buildings:
        print(i)
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
                    #print(item["Path"] + "\n" + str(item["Value"]["Value"]))
                    usage1 = item["Value"]["Value"]

            time2 = requests.get(response.json()["Links"]["Value"] + "?time=*-1w", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            for item in time2.json()["Items"]:
                if item["Name"] == "Cumulative Use":
                    #print(item["Path"] + "\n" + str(item["Value"]["Value"]))
                    usage2 = item["Value"]["Value"]

            time3 = requests.get(response.json()["Links"]["Value"] + "?time=*-2w", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            for item in time3.json()["Items"]:
                if item["Name"] == "Cumulative Use":
                    #print(item["Path"] + "\n" + str(item["Value"]["Value"]))
                    usage3 = item["Value"]["Value"]
            print(str(usage1) + " " + str(usage2) + " " + str(usage3))
            if (usage2 - usage3 != 0):
                print((usage1 - usage2)/(usage2 - usage3))
                dictionary[assetNo] = (usage1 - usage2)/(usage2 - usage3)
                #print(j)
                #j = j + 1
            else:
                if (usage1 - usage2 == 0):
                    dictionary[assetNo] = 1
                    #print(j)
                    #j = j + 1
                else:
                    dictionary[assetNo] = 2
                    #print(j)
                    #j = j + 1
    return dictionary


class locations(Resource):
    def get(self):
        # dictionary = ottoCode()
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "static/", "data1.json")
        data = json.load(open(json_url))
        # newData = []
        # for element in data:
        #     if element['assetNumber'] in dictionary.keys():
        #        element['val'] = dictionary[element['assetNumber']]
        #        newData.append(element)


        # print(newData)
        return data, 200

@app.route('/')
# @crossdomain(origin='*')
# @cross_origin()
def hello_world():
    return render_template('feature_layer.html')


@app.route('/vis')
def show():
    return render_template('visualization.html')

@app.route('/ha',methods=['GET'])
def otto():
    url = 'https://bldg-pi-api.ou.ad3.ucdavis.edu/piwebapi/search/query?q=afelementtemplate:Domestic%20AND%20afelementtemplate:Water%20AND%20afelementtemplate:Gal%20NOT%20afelementtemplate:Manual&fields=name;links&count=100'
    #headers = {'Content-Type': 'application/json'}

    #filters = [dict(name='name', op='like', val='%y%')]
    #params = dict(q=json.dumps(dict(filters=filters)))

    response = requests.get(url, auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))#, params=params)
    #assert response.status_code == 200
    buildings = response.json()["Items"]
    i = 0
    j = 0
    dictionary = {}
    for building in buildings:
        print(i)
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
                    #print(item["Path"] + "\n" + str(item["Value"]["Value"]))
                    usage1 = item["Value"]["Value"]

            time2 = requests.get(response.json()["Links"]["Value"] + "?time=*-1w", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            for item in time2.json()["Items"]:
                if item["Name"] == "Cumulative Use":
                    #print(item["Path"] + "\n" + str(item["Value"]["Value"]))
                    usage2 = item["Value"]["Value"]

            time3 = requests.get(response.json()["Links"]["Value"] + "?time=*-2w", auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
            for item in time3.json()["Items"]:
                if item["Name"] == "Cumulative Use":
                    #print(item["Path"] + "\n" + str(item["Value"]["Value"]))
                    usage3 = item["Value"]["Value"]
            print(str(usage1) + " " + str(usage2) + " " + str(usage3))
            if (usage2 - usage3 != 0):
                print((usage1 - usage2)/(usage2 - usage3))
                dictionary[assetNo] = (usage1 - usage2)/(usage2 - usage3)
                #print(j)
                #j = j + 1
            else:
                if (usage1 - usage2 == 0):
                    dictionary[assetNo] = 1
                    #print(j)
                    #j = j + 1
                else:
                    dictionary[assetNo] = 2
                    #print(j)
                    #j = j + 1
    return dictionary

api.add_resource(locations, '/locations')

if __name__ == "__main__":
    app.run()