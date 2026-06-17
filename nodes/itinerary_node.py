from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)

def itinerary_node(state):
    prompt = f"""
Create itinerary for {state['city']}
Attractions: {state['attractions']}
Restaurants: {state['restaurants']}
Weather: {state['weather_forecast']}
"""

    res = llm.invoke(prompt)

    return {"itinerary": {"raw": res.content}}