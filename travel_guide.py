# CAPSTONE PROJECT: GPT-APP DEVELOPMENT (AI TRAVEL GUIDE EXPLAINER)

# %%
#Importing libraries
import os
import openai 
import streamlit as st
from dotenv import load_dotenv
from IPython.display import HTML, display

# %%
#Set up your OpenAI API key
load_dotenv()
api_key = os.getenv("KEY")
# %%
#Travel Guide Explainer
# ### My ideal travel guide explainer:
# 1. Best time to visit
# 2. Attractions
# 3. Cuisine
# 4. Language

# %%
#Building a customize travel guide explainer
input = """

Paris

"""

example = """
1. Best Time to Visit: The best time to visit Paris is generally in the spring (April to June) 
or fall (September to November) when the weather is mild, and the tourist crowds are smaller compared to the peak summer months.

2. Attractions: Paris is famous for its iconic landmarks such as the Eiffel Tower, Louvre Museum, Notre-Dame Cathedral,
Montmartre, Champs-Élysées, and many more.

3. Cuisine: Paris is a food lover's paradise. Don't miss the chance to try French cuisine, including croissants, escargot,
coq au vin, crème brûlée, and more. Explore local cafes, bistros, and patisseries for an authentic experience.

4. Language: The official language is French. While many people in the tourist areas speak English, it's always helpful to learn some basic
French phrases for better communication. A simple "Excusez-moi" (excuse me) or "pardon," "Bonjour" (hello) and "Merci" (thank you) can go a 
long way in showing respect.

"""

user_input = """

Japan


"""

#Create a request to ChatCompletion endpoint
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{

            "role":"system",
                 "content": """You are the funniest, experienced personal travel guide explainer who has travelled to every part of the world,
                              please explain to me when is the best time to visit, attractions, cuisine, and lastly language insights in a short
                              but informative one. """},
            {
            "role": "user",
            "content": input},
            
            {
            "role":"assistant", #Example answer your system would give
            "content": example},

            {
            "role":"user",
            "content": user_input

            }

    ],
    max_tokens = 1000,
    temperature = 1
)
display(response['choices'][0]['message']['content'])

# %%
# Generate images using DALL-E
prompt = f"A HD photo of famous landmark in {user_input} captured by a professional,competition winner photographer using a high quality camera in 2023"
response = openai.Image.create(
    model="image-alpha-001",
    prompt=prompt,
    n=2,
    size="256x256"

    )
image_urls = [data['url'] for data in response['data']]
