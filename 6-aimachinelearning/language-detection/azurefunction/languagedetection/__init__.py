import logging
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    key = "b2fc9abbea61406bbf3fa9b52e98669d"
    endpoint = "https://pyt21-textanalyticsservices.cognitiveservices.azure.com/"

    cred = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=cred)

    req_body = req.get_json()

    text = [req_body.get('text')]
    res = client.detect_language(documents = text)[0]
    return func.HttpResponse(res.primary_language["iso6391_name"])