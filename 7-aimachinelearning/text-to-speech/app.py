# pip install azure.cognitiveservices.speech
import azure.cognitiveservices.speech as speechsdk

key = "6554e101dc014474a6507dc8e4dc0f96"
region = "westeurope"

speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config = speech_config)

print("Type something...")
text = input()

result = speech_synthesizer.speak_text(text)
