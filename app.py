import streamlit as st
from graph import app
from extractor import extract_trip_info, get_missing_fields, QUESTIONS
from db import init_db, save_trip, load_trips

init_db()

st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")
st.title("✈️ AI Travel Planner")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "travel_data" not in st.session_state:
    st.session_state.travel_data = {}

if "history" not in st.session_state:
    st.session_state.history = load_trips()

# CHAT UI
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Plan your trip...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    if not st.session_state.travel_data:
        extracted = extract_trip_info(user_input).model_dump()
        st.session_state.travel_data.update({k:v for k,v in extracted.items() if v})

    missing = get_missing_fields(st.session_state.travel_data)

    if missing:
        field = missing[0]
        st.session_state.messages.append({
            "role": "assistant",
            "content": QUESTIONS[field]
        })
        st.rerun()

    with st.spinner("Generating itinerary..."):
        result = app.invoke(st.session_state.travel_data)

    itinerary = result.get("formatted_itinerary","Error")

    st.session_state.messages.append({"role":"assistant","content":itinerary})

    save_trip(st.session_state.travel_data, itinerary)

    st.rerun()