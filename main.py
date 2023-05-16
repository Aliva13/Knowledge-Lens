# Python program to read
# json file


import json

# Opening JSON file
f = open('input.json', "r")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
myList = []
for i in data['parametersList']:
    myDict = {
        "parameterName": i['parameterName'],
        "max": i['max'],
        "min": i['min'],
        "avg": i['avg']
    }
    myList.append(myDict)
new_list = json.dumps(myList)

with open("input.json", "w") as file1:
    file1.write(new_list)
print(myList)

# Closing file
f.close()
