from pydantic import BaseModel
from typing import Optional, List
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    api_key=GROQ_API_KEY
)

class UserInput(BaseModel):
    source: Optional[str]
    destination: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    budget: Optional[str]
    trip_type: Optional[str]
    interests: Optional[List[str]]

extractor_llm = llm.with_structured_output(UserInput)

def extract_trip_info(message: str):

    prompt = f"""
Extract travel data.

IMPORTANT:
- Convert dates into YYYY-MM-DD
- Example: "20 June 2026" → "2026-06-20"

User: {message}
"""

    return extractor_llm.invoke(prompt)


REQUIRED_FIELDS = [
    "source","destination","start_date","end_date",
    "budget","trip_type","interests"
]

def get_missing_fields(data):
    return [f for f in REQUIRED_FIELDS if not data.get(f)]

QUESTIONS = {
    "source": "🌍 Where are you travelling from?",
    "destination": "📍 Where do you want to travel?",
    "start_date": "📅 Start date?",
    "end_date": "📅 End date?",
    "budget": "💰 Budget?",
    "trip_type": "👨‍👩‍👧 Trip type?",
    "interests": "🎯 Interests?"
}