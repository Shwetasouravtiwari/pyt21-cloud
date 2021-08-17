import logging
import json
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    key = "b2fc9abbea61406bbf3fa9b52e98669d"
    endpoint = "https://pyt21-textanalyticsservices.cognitiveservices.azure.com/"

    cred = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=cred)

    req_body = req.get_json()
    document = [req_body.get('text')]
    res = client.analyze_sentiment(documents = document)[0]

    print("Sentiment: {}".format(res.sentiment))
    print("Positive Store: {0:.2f}\nNeutral Store: {1:.2f}\nNegative Store: {2:.2f}".format(res.confidence_scores.positive, res.confidence_scores.neutral, res.confidence_scores.negative))
    print('\n\n')

    data = {
        "sentiment": res.sentiment,
        "confidenceScores": {
            "positive": res.confidence_scores.positive,
            "neutral": res.confidence_scores.neutral,
            "negative": res.confidence_scores.negative
        }
    }

    return func.HttpResponse(json.dumps(data))