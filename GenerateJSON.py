import json
import pyperclip



dataList = []

dataId = 0
Datadate = ''
addingData = True



# Data to be written



while addingData == True:
    Datadate = input()
    dataId += 1
    Datadate = Datadate[0:4] + '-' + Datadate[4:6] + '-' + Datadate[6:8]
    print(Datadate)
    dictionary = {
    "id": dataId,
    "date": Datadate,
    "cultureList": [
        {
            "culture": 'en',
            'title': '',
            "desc" : ''
        },
        {
            "culture": 'zh-CHS',
            'title': '',
            "desc" : ''
        },
        {
            "culture": 'zh-CHT',
            'title': '',
            "desc" : ''
        }
    ],
    }
    if(Datadate == "q--"):
        break;

    dataList.append(dictionary)
   #f addingData += 1
    



dataList.reverse()
# Serializing json
json_object = json.dumps(dataList, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)