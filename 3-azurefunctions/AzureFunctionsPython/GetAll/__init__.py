import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, cosmos: func.DocumentList) -> func.HttpResponse:
    products = []

    for product in cosmos:
        p_dict = {
            "id": product['id'],
            "name": product['name'],
            "description": product['description'],
            "category": product['category']
        }
        products.append(p_dict)

    return func.HttpResponse(
        json.dumps(products),
        status_code=200,
        mimetype="application/json"
    )
    