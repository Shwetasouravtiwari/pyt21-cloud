#pip install azure.cognitiveservices.vision.computervision
#pip install pillow
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
from PIL import Image
import os
import sys
import time

subscription_endpoint = "https://pyt21-computervision.cognitiveservices.azure.com/"
subscription_key = "b8559850413b48eead3b36140ff4ac1a"

client = ComputerVisionClient(subscription_endpoint, CognitiveServicesCredentials(subscription_key))
image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

local_image_path = os.path.join(image_folder, "pexels-brian-lazo-9160980.jpg")
local_image = open(local_image_path, "rb")

remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
image_features = ["categories"]

description_result = client.describe_image_in_stream(local_image)
categorize_results_remote = client.analyze_image(remote_image_url, image_features)

print("===== Description an image - local =====")
if len(description_result.captions) == 0:
    print("No descriptions detected")
else:
    for caption in description_result.captions:
        print("'{}' width confidence {:.2f}%".format(caption.text, caption.confidence * 100))
print()


print("===== Categorize an image - remote =====")
if (len(categorize_results_remote.categories) == 0):
    print("No categories detected.")
else:
    for category in categorize_results_remote.categories:
        print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))