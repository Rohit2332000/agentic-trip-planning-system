from langgraph.graph import StateGraph, END
from models.state import TravelState

from nodes.orchestrator import orchestrator
from nodes.travel_node import travel_node
from nodes.weather_node import weather_node
from nodes.hotel_node import hotel_node
from nodes.itinerary_node import itinerary_node
from nodes.format_node import format_itinerary_node
from nodes.transportation_node import transportation_node

graph = StateGraph(TravelState)

graph.add_node("orchestrator", orchestrator)
graph.add_node("travel", travel_node)
graph.add_node("weather", weather_node)
graph.add_node("hotel", hotel_node)
graph.add_node("transport", transportation_node)
graph.add_node("itinerary", itinerary_node)
graph.add_node("format", format_itinerary_node)

graph.set_entry_point("orchestrator")

graph.add_edge("orchestrator", "travel")
graph.add_edge("orchestrator", "weather")
graph.add_edge("orchestrator", "hotel")
graph.add_edge("orchestrator", "transport")

graph.add_edge("travel", "itinerary")
graph.add_edge("weather", "itinerary")
graph.add_edge("hotel", "itinerary")
graph.add_edge("transport", "itinerary")

graph.add_edge("itinerary", "format")
graph.add_edge("format", END)

app = graph.compile()