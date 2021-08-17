import logging
import requests
import uuid
import json

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"
    subscription_key = "40b8ea00432441d697ff72d67617ec8c"
    location = "westeurope"

    req_body = req.get_json()

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-Type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    params = { 
        'api-version': '3.0', 
        'from': req_body.get('from'), 
        'to': req_body.get('to')
    }
    body =[{ 'text': req_body.get('text') }]

    res = requests.post(endpoint, params=params, headers=headers, json=body)
    data = res.json()

    if data:
        return func.HttpResponse(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ':')))
    else:
        return func.HttpResponse("Invalid request", status_code=400)
    