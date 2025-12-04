import os
from google import genai
from google.genai import types
from PIL import Image
from classes import textGeneratedContent

# 1. Set your API key (or set it in your environment variables)
# os.environ['GOOGLE_API_KEY'] = 'YOUR_API_KEY' 

# 2. Initialize the client (Synchronous is easier for scripts)
client = genai.Client(api_key="AIzaSyAiF4UlZ0P3j7qJ-Vrok_8CXoYTSpM2cDk")

height_input = input("What is your height?\n")
body_shape = input("What is your body shape?\n")
skin_tone = input("What is your skintone?\n")
under_tone = input("What is your undertone?\n")

body_features = {"height": height_input, "shape": body_shape, "skin_tone": skin_tone, "under_tone": under_tone}


#3. Create the prompt

textGeneratedContent = textGeneratedContent(body_features["height"], body_features["shape"], body_features["skin_tone"], body_features["under_tone"])

def recommendation_response_one():
    response_one = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=textGeneratedContent.HeightAndBodyReason(body_features["height"], body_features["shape"]))
    return response_one

def recommendation_response_two():
    response_two = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=textGeneratedContent.SkintoneAndUndertoneReason(body_features["skin_tone"], body_features["under_tone"]))
    return response_two

def final_recommendation_response():
    final_response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=textGeneratedContent.FeatureCombinationReason(firstCombination=recommendation_response_one(), secondCombination=recommendation_response_two()))
    return final_response

# 4. Print the result
print(final_recommendation_response().text)