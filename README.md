# ✈️ AI Travel Planner — Multi-Agent Travel Intelligence System

## Overview

AI Travel Planner is a production-style, multi-agent travel planning system built with **LangGraph**, **LLMs**, and **real-time APIs**. Instead of relying on a single prompt, the application decomposes travel planning into specialized agents that collaborate to generate personalized, day-wise itineraries.

The system combines reasoning, tool calling, state management, and external APIs to deliver accurate and context-aware travel recommendations.

---

## Key Features

* 🤖 Multi-agent orchestration using LangGraph
* 🧠 LLM-powered itinerary generation
* 🌍 Destination understanding and travel recommendations
* 🌦 Real-time weather forecasts
* 🏨 Hotel recommendations
* 🍽 Restaurant discovery
* 📍 Tourist attraction search
* 🚗 Route and transportation planning
* 💾 Persistent trip history with SQLite
* 📄 Markdown itinerary generation
* 📥 Downloadable travel plans

---

# Architecture

```
User (Streamlit)
      │
      ▼
Input Extraction (LLM)
      │
      ▼
LangGraph Orchestrator
      │
 ┌────┼────────┬─────────┬─────────────┐
 ▼    ▼        ▼         ▼
Travel Weather Hotel Transportation
Agent  Agent   Agent      Agent
      │
      ▼
Itinerary Generator (LLM)
      │
      ▼
Formatter
      │
      ▼
SQLite + Download
```

---

# Agent Workflow

### Travel Agent

* Discovers attractions and restaurants
* Searches destination-specific activities

### Weather Agent

* Retrieves live weather forecasts
* Adds weather-aware recommendations

### Hotel Agent

* Suggests accommodations near the destination

### Transportation Agent

* Calculates routes
* Recommends travel modes
* Estimates distances

### Itinerary Generator

* Combines outputs from all agents
* Produces a structured day-wise travel plan

---

# AI & Orchestration

* **LangGraph** for stateful multi-agent workflows
* **Groq LLMs (Llama/Qwen)** for reasoning and itinerary generation
* **Pydantic** for structured outputs and validation
* Parallel agent execution with deterministic graph orchestration

---

# External Tools

* Geoapify — Geocoding & Places
* OpenWeather — Weather Forecasts
* OpenRouteService — Routing & Distance
* Tavily Search — Web Search

---

# Tech Stack

**AI**

* LangGraph
* LangChain
* Groq LLM
* Pydantic

**Backend**

* Python
* SQLite

**Frontend**

* Streamlit

**APIs**

* Geoapify
* OpenWeather
* OpenRouteService
* Tavily

---

# Production Features

* Modular architecture
* Stateful agent execution
* Persistent memory with SQLite
* API retry & graceful error handling
* Structured JSON validation
* Downloadable itineraries
* Multi-session support

---

# Project Structure

```
TravelPlanner/
│── app.py
│── graph.py
│── db.py
│── extractor.py
│── config.py
│
├── models/
│   └── state.py
│
├── nodes/
│   ├── orchestrator.py
│   ├── travel_node.py
│   ├── weather_node.py
│   ├── hotel_node.py
│   ├── transportation_node.py
│   ├── itinerary_node.py
│   └── format_node.py
│
├── services/
│   ├── geo.py
│   ├── weather.py
│   ├── attractions.py
│   ├── restaurants.py
│   └── transport.py
│
└── README.md
```

---

# Example Workflow

User Request:

> *Plan a 5-day budget trip to Manali from Delhi.*

The system:

1. Extracts structured travel details using an LLM.
2. Identifies missing information and requests clarification if needed.
3. Executes multiple agents in parallel.
4. Retrieves live weather, attractions, hotels, and routing data.
5. Generates a personalized itinerary.
6. Formats the output and stores it for future access.

---

# Future Improvements

* User authentication
* Interactive maps (Leaflet/Folium)
* Flight and train booking integration
* Budget optimization
* Docker deployment
* Cloud-native deployment
* Human-in-the-loop itinerary editing

---

# Skills Demonstrated

* Multi-Agent AI Systems
* LangGraph Orchestration
* Tool Calling
* Stateful Workflows
* Retrieval-Augmented Generation (RAG)
* API Integration
* LLM Engineering
* FastAPI/Streamlit Development
* Production-Ready AI Architecture

---

## Author

**Rohit Kumar Yadav**

AI/ML Engineer | Generative AI | LLMs | Agentic AI | LangGraph | LangChain
