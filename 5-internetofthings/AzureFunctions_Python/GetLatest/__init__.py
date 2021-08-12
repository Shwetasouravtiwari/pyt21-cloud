import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, cosmos:func.DocumentList) -> func.HttpResponse:

    items = []

    for item in cosmos:
        item_dict = {
           "temperature": item['temperature'],
           "humidity": item['humidity']
        }
        items.append(item_dict)

    return func.HttpResponse(
            json.dumps(items[0]),
            status_code=200,
            mimetype="application/json"   
    )