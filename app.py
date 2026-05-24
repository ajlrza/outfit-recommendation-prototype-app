import os
from google import genai
from google.genai import types
from PIL import Image
from classes import textGeneratedContent

client = genai.Client(api_key="")

sex = input("What is your sex?\n")
height_input = input("What is your height?\n")
body_shape = input("What is your body shape?\n")
skin_tone = input("What is your skintone?\n")
under_tone = input("What is your undertone?\n")

body_features = {"sex": sex, "height": height_input, "shape": body_shape, "skin_tone": skin_tone, "under_tone": under_tone}


textGeneratedContent = textGeneratedContent(body_features["height"], body_features["shape"], body_features["skin_tone"], body_features["under_tone"])

def recommendation_response_one():
    response_one = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=textGeneratedContent.HeightAndBodyReason(body_features["sex"], body_features["height"], body_features["shape"]))
    return response_one

def recommendation_response_two():
    response_two = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=textGeneratedContent.SkintoneAndUndertoneReason(body_features["skin_tone"], body_features["under_tone"]))
    return response_two

def final_recommendation_response():
    rec_one = recommendation_response_one()
    rec_two = recommendation_response_two()
    
    prompt_text = textGeneratedContent.FeatureCombinationReason(
        firstCombination=rec_one, 
        secondCombination=rec_two
    )
    
    prompt_text += """
    \n
    Based on the analysis above, create 3 distinct outfit combinations. 
    For each item in the outfit:
    1. Provide the specific product name.
    2. Suggest a popular retailer (e.g., Uniqlo, Zara, H&M, or local equivalents).
    3. search for the actual item to ensure it exists.
    """

    final_response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt_text,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())], 
            response_modalities=["TEXT"]
        )
    )
    return final_response

print(final_recommendation_response().text)
