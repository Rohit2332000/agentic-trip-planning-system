import requests
from config import GEOAPIFY_API_KEY
from services.geo import get_coordinates

def hotel_node(state):
    coords = get_coordinates(state["city"])

    if not coords:
        return {"hotels": []}

    lat, lon = coords

    url = f"https://api.geoapify.com/v2/places?categories=accommodation.hotel&filter=circle:{lon},{lat},5000&limit=5&apiKey={GEOAPIFY_API_KEY}"

    res = requests.get(url).json()

    hotels = [
        {
            "name": f["properties"].get("name"),
            "address": f["properties"].get("formatted")
        }
        for f in res.get("features", [])
    ]

    return {"hotels": hotels}