# pip install azure-ai-textanalytics

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "b2fc9abbea61406bbf3fa9b52e98669d"
endpoint = "https://pyt21-textanalyticsservices.cognitiveservices.azure.com/"

def connect():
    cred = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=cred)
    return client

def sentiment_analysis(client:TextAnalyticsClient):
    text = ["what is your problem?! Why must you smoke? It smells bad. But for all you other people that don't smoke. thank you."]
    
    res = client.analyze_sentiment(documents = text)[0]
    print("Sentiment: {}".format(res.sentiment))
    print("Positive Store: {0:.2f}\nNeutral Store: {1:.2f}\nNegative Store: {2:.2f}".format(res.confidence_scores.positive, res.confidence_scores.neutral, res.confidence_scores.negative))
    print('\n\n')

    for idx, sentence in enumerate(res.sentences):
        print("Sentence Text: {}".format(sentence.text))
        print("Sentence {} Sentiment: {}".format(idx+1, sentence.sentiment))
        print("Positive Store: {0:.2f}\nNeutral Store: {1:.2f}\nNegative Store: {2:.2f}".format(sentence.confidence_scores.positive, sentence.confidence_scores.neutral, sentence.confidence_scores.negative))
        print('\n\n')




client = connect()
sentiment_analysis(client)