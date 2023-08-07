#Streamlit app for deployment
import os
import openai
import pandas as pd
import streamlit as st
#from dotenv import load_dotenv
#from IPython.display import HTML, display

# Set up your OpenAI API key
#load_dotenv()
os.environ.get("KEY")

# Define the Streamlit app
def main():
    st.title("Travel Guide Explainer")
    
    # Add a quiz to determine the user's travel style
    st.sidebar.header("What's your travel style?")
    travel_styles = ["Adventure", "Relaxation", "Culture", "Food"]
    travel_style = st.sidebar.radio("Choose one:", travel_styles)
    
    # Provide personalized recommendations based on the user's travel style
    if travel_style == "Adventure":
        st.sidebar.subheader("Looking for an adventure?")
        st.sidebar.write("Here are some destinations that are perfect for thrill-seekers:")
        adventure_destinations = {
            "New Zealand": "Known for its stunning natural beauty and outdoor activities such as hiking, skiing, and bungee jumping.",
            "Costa Rica": "A paradise for eco-tourists, with activities such as zip-lining, rafting, and wildlife watching.",
            "South Africa": "A diverse country with opportunities for safari, surfing, and mountain climbing."
        }
        df = pd.DataFrame(adventure_destinations.items(),columns=["Destination","Description"])
        st.sidebar.table(df.set_index("Destination"))
        
    elif travel_style == "Relaxation":
        st.sidebar.subheader("Need some rest and relaxation?")
        st.sidebar.write("Here are some destinations that are perfect for unwinding:")
        relaxation_destinations = {
            "Maldives": "An island nation known for its crystal-clear waters and overwater bungalows.",
            "Bali": "An Indonesian island with beautiful beaches, rice terraces, and temples.",
            "Hawaii": "A US state with stunning beaches, waterfalls, and volcanoes."
        }
        df = pd.DataFrame(relaxation_destinations.items(),columns=["Destination","Description"])
        st.sidebar.table(df.set_index("Destination"))
    elif travel_style == "Culture":
        st.sidebar.subheader("Interested in culture and history?")
        st.sidebar.write("Here are some destinations that are rich in cultural heritage:")
        culture_destinations = {
            "Italy": "A country with a rich history and culture, known for its art, architecture, and cuisine.",
            "Japan": "A country with a unique culture and traditions, known for its temples, gardens, and cuisine.",
            "Egypt": "A country with a rich history dating back to ancient times, known for its pyramids, temples, and museums."
        }
        df = pd.DataFrame(culture_destinations.items(), columns=["Destination", "Description"])
        st.sidebar.table(df.set_index("Destination"))
    elif travel_style == "Food":
        st.sidebar.subheader("Love trying new foods?")
        st.sidebar.write("Here are some destinations that are known for their cuisine:")
        food_destinations = {
            "Thailand": "A country with a diverse and flavorful cuisine, known for its curries, noodles, and street food.",
            "France": "A country with a rich culinary tradition, known for its pastries, cheese, and wine.",
            "Mexico": "A country with a vibrant and colorful cuisine, known for its tacos, tamales, and tequila."
        }
        df = pd.DataFrame(food_destinations.items(), columns=["Destination", "Description"])
        st.sidebar.table(df.set_index("Destination"))
    
    destination_input = st.text_area("Please enter your destination here:", height=200)
    if st.button("Recommend me"):
        explanation,image_urls = explain_travel(destination_input)
        st.subheader(f"Recommendations for {destination_input}")
        st.write(explanation)
        cols = st.columns(2)
        for i, image_url in enumerate(image_urls):
            cols[i].image(image_url, caption=f"📷")

# Define a function to get the explanation
def explain_travel(user_input):
    # Use OpenAI ChatCompletion API to get the explanation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """You are the funniest, experienced personal travel guide explainer who has travelled to every part of the world,
                              please explain to me when is the best time to visit, attractions, cuisine, and lastly language insights in a short
                              but informative one. """
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        max_tokens=1000,
        temperature=1
    )
    explanation = response['choices'][0]['message']['content']
    
     # Generate images using DALL-E
    prompt = f"A realistic HD photo of famous landmark in {user_input} captured by a professional,competition winner photographer using a high quality camera in 2023"
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        n=2,
        size="256x256"
    )
    image_urls = [data['url'] for data in response['data']]

    return explanation, image_urls
    

if __name__ == "__main__":
    main()
