# pip install azure-ai-textanalytics

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "b2fc9abbea61406bbf3fa9b52e98669d"
endpoint = "https://pyt21-textanalyticsservices.cognitiveservices.azure.com/"

def connect():
    cred = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=cred)
    return client

def language_detection(client:TextAnalyticsClient):
    try:
        text = ['Vilket språk är det här?']
        res = client.detect_language(documents = text)[0]
        print('Language: ', res.primary_language["iso6391_name"])
    except Exception as error:
        print('Error:: {}'.format(error) )

client = connect()
language_detection(client)
