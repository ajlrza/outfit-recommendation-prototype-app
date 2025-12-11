import os
from google import genai
from google.genai import types
from PIL import Image
from classes import textGeneratedContent

# 1. Set your API key (or set it in your environment variables)
# os.environ['GOOGLE_API_KEY'] = 'YOUR_API_KEY' 

# 2. Initialize the client (Synchronous is easier for scripts)
client = genai.Client(api_key="")

sex = input("What is your sex?\n")
height_input = input("What is your height?\n")
body_shape = input("What is your body shape?\n")
skin_tone = input("What is your skintone?\n")
under_tone = input("What is your undertone?\n")

body_features = {"sex": sex, "height": height_input, "shape": body_shape, "skin_tone": skin_tone, "under_tone": under_tone}

#3. Create the prompt

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

# Update your final function to include tools
def final_recommendation_response():
    # 1. Get the reasoning from previous steps
    rec_one = recommendation_response_one()
    rec_two = recommendation_response_two()
    
    # 2. Construct a specific prompt for the final step
    # We combine the previous insights + the instruction to search
    prompt_text = textGeneratedContent.FeatureCombinationReason(
        firstCombination=rec_one, 
        secondCombination=rec_two
    )
    
    # Append the "Shopping" instruction
    prompt_text += """
    \n
    Based on the analysis above, create 3 distinct outfit combinations. 
    For each item in the outfit:
    1. Provide the specific product name.
    2. Suggest a popular retailer (e.g., Uniqlo, Zara, H&M, or local equivalents).
    3. search for the actual item to ensure it exists.
    """

    final_response = client.models.generate_content(
        model="gemini-2.5-pro", # Use Pro for better reasoning/search
        contents=prompt_text,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())], # <--- THIS IS KEY
            response_modalities=["TEXT"]
        )
    )
    return final_response

# 4. Print the result
print(final_recommendation_response().text)
