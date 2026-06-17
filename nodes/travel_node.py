from services.attractions import get_attractions
from services.restaurants import get_restaurants

def travel_node(state):
    return {
        "attractions": get_attractions(state["city"]),
        "restaurants": get_restaurants(state["city"]),
        "overview": f"Travel guide for {state['city']}"
    }