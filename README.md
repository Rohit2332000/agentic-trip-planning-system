✈️ AI Travel Planner (Agentic System using LangGraph)
🧠 Overview

The AI Travel Planner is an agent-based travel intelligence system that generates personalized, multi-day travel itineraries using LangGraph orchestration, LLMs, and real-world APIs.

The system decomposes travel planning into multiple intelligent agents (weather, attractions, hotels, transport, itinerary generation) and combines their outputs into a structured, user-friendly travel guide.

🚀 Live Features
🧳 AI-powered travel itinerary generation
🌍 Smart destination understanding
🌦 Real-time weather forecasting
📍 Tourist attractions discovery
🍽 Restaurant recommendations
🏨 Hotel suggestions near location
🚗 Transportation planning (distance + mode recommendation)
📄 Markdown-style itinerary generation
💾 SQLite travel history storage
📥 Downloadable itineraries
🏗️ System Architecture
User (Streamlit UI)
        │
        ▼
Input Extraction (LLM Parser)
        │
        ▼
LangGraph Orchestrator (DAG Engine)
        │
 ┌──────┼───────────┬─────────────┬────────────┐
 ▼      ▼           ▼             ▼            ▼
Travel  Weather   Hotel    Transportation  External APIs
Agent    Agent     Agent        Agent
        │
        ▼
Itinerary Generator (LLM)
        │
        ▼
Formatter (UI Optimized Output)
        │
        ▼
SQLite Storage + Download
⚙️ Tech Stack
🧠 AI / LLM
LangGraph
Groq LLM (Llama / Qwen models)
Structured LLM output (Pydantic)
🌐 APIs
Geoapify (Geocoding + Places)
OpenWeather API
OpenRouteService (Routing)
Tavily Search API
🖥️ Backend
Python
SQLite (persistent storage)
🎨 Frontend
Streamlit
🧠 System Design Highlights
🔹 1. Agent-Based Architecture

Each task is handled by independent agents:

Travel Agent → Attractions & restaurants
Weather Agent → Forecasting
Hotel Agent → Accommodation search
Transport Agent → Route optimization
🔹 2. LangGraph DAG Execution
Parallel execution of nodes
Controlled data flow
Deterministic pipeline execution
🔹 3. Tool-Augmented LLM System

LLMs are combined with real APIs:

Web search (Tavily)
Maps & geolocation (Geoapify)
Weather data (OpenWeather)
Route optimization (ORS)
🔹 4. Fault-Tolerant Design
Safe JSON parsing
API failure handling
Graceful degradation for missing data
🔹 5. Persistent Memory
SQLite stores user trips
Downloadable travel history
Multi-session support
📁 Project Structure
TravelPlanner/
│
├── app.py                  # Streamlit frontend
├── graph.py                # LangGraph pipeline
├── db.py                   # SQLite storage
├── extractor.py           # LLM-based input parsing
├── config.py              # API keys
│
├── models/
│   └── state.py           # TravelState schema
│
├── nodes/
│   ├── orchestrator.py
│   ├── travel_node.py
│   ├── weather_node.py
│   ├── hotel_node.py
│   ├── itinerary_node.py
│   ├── format_node.py
│   ├── transportation_node.py
│
├── services/
│   ├── geo.py
│   ├── weather.py
│   ├── attractions.py
│   ├── restaurants.py
│   ├── transport.py
│
├── .env
└── README.md
⚙️ Installation
git clone https://github.com/your-username/TravelPlanner.git
cd TravelPlanner

pip install -r requirements.txt
🔑 Environment Variables (.env)
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
GEOAPIFY_API_KEY=your_key
OPENWEATHER_API_KEY=your_key
ORS_API_KEY=your_key
▶️ Run the Project
streamlit run app.py
🧪 Example Workflow

User enters:

"Plan a 5-day trip to Manali from Delhi under budget"

System:
Extracts structured input using LLM
Identifies missing fields (if any)
Calls multiple agents in parallel
Fetches real-time data from APIs
Generates itinerary using LLM
Formats output into travel guide
📊 Output Example
Day-wise itinerary
Places to visit
Restaurants
Weather insights
Safety tips
Transport suggestions
🧠 Key Innovations
🔹 Multi-agent LangGraph pipeline
🔹 Real-time API + LLM hybrid system
🔹 Structured travel intelligence system
🔹 Parallel node execution (DAG)
🔹 Production-style modular architecture
📌 Future Improvements
🔥 User authentication system
🔥 Map visualization (Leaflet / Folium)
🔥 Live flight pricing API
🔥 Mobile-friendly UI
🔥 Deployment (Docker + Cloud)
🏆 Project Impact

This project demonstrates:

Advanced LLM orchestration
Real-world system design skills
API integration at scale
Production-grade modular architecture
End-to-end AI product development
👨‍💻 Author

Rohit Yadav
AI/ML Engineer | Data Science Enthusiast