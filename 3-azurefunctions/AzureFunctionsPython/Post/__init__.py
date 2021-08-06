import logging
import uuid
import azure.functions as func


def main(req: func.HttpRequest, cosmos: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()

    if req_body:
        products = func.DocumentList()

        product = {
            "id": str(uuid.uuid4()),
            "name": req_body.get('name'),
            "description": req_body.get('description'),
            "category": req_body.get('category'),
        }

        products.append(func.Document.from_dict(product))
        cosmos.set(products)

        return func.HttpResponse(f"Product added")

    else:
        return func.HttpResponse(
             "something went wrong",
             status_code=400
        )
