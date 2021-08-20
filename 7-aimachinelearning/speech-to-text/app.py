# pip install azure.cognitiveservices.speech
import azure.cognitiveservices.speech as speechsdk

key = "6554e101dc014474a6507dc8e4dc0f96"
region = "westeurope"

speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config = speech_config)

print("Say something...")
result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized.")