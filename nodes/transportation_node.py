from services.transport import get_route

def transportation_node(state):
    dist, duration = get_route(state["source"], state["destination"])

    return {
        "transportation": {
            "distance_km": dist,
            "duration_hr": duration
        }
    }