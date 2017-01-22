import json

with open('data.json') as data_file:
    data = json.load(data_file)

for element in data:
    #deleteList = ['bldgKey', "officialName", "ucdhsBldgNum", "location", "affiliation", "category", "primaryUse", "address", "city", "county", "state", "zip", "countryCode", "addressCode", "occupied", "onOffCampus", "cefaName", "cefaFireResistConsTypCd", "planning", "condition", "defaultOMPElig", "ompEligMethod", "ownership", "floors", "height", "footprint", "perimeter", "basicGross", "cuGross", "circulation", "custodial", "mechanical", "parking", "toilet", "nasf", "asf", "spaceCount", "netUsable", "structural", "outsideGross", "relatedGross", "maintainedGross", "janitorized", "constructed", "renovated", "vacated", "demolished", "ompEligSummary"]
    newList = ["facilitiesCode"]
    for i in newList:
        del element[i]


with open('data1.json', 'w') as data_file:
    data = json.dump(data, data_file)