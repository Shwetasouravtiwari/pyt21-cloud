import requests
# If you are using Python 3+, import urllib instead of urllib2

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["temperature", "humidity"],
                    "Values": [ [ "10", "78" ] ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/713ead5c2bfe447d8c1bdd33c5cfbe4c/services/002375edbf2b4f8eb52aa3413c4d45db/execute?api-version=2.0&details=true'
api_key = 'uCYRW6gpjy231XtJAyqDE1qtMTzklVoM+jRLewVlACnH+jqOhF4MQYIDA5lBI/Uu/TFpgfL0LCOXsuwPfToqWA==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

res = requests.post(url, headers=headers, data = data)
result = res

print(result) 
