import requests
import uuid
import json

endpoint = "https://api.cognitive.microsofttranslator.com/"
subscription_key = "40b8ea00432441d697ff72d67617ec8c"
location = "westeurope"
path = "/translate"
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-Type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

params = { 'api-version': '3.0', 'from': 'sv', 'to': ['de'] }
body =[{ 'text': 'Det här jag skriver nu är svenska' }]

response = requests.post(constructed_url, params=params, headers=headers, json=body)
data = response.json()

print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ':')))