import requests
from config import GEOAPIFY_API_KEY
from services.geo import get_coordinates

def get_restaurants(city: str):
    coords = get_coordinates(city)
    if not coords:
        return []

    lat, lon = coords

    url = f"https://api.geoapify.com/v2/places?categories=catering.restaurant&filter=circle:{lon},{lat},5000&limit=5&apiKey={GEOAPIFY_API_KEY}"

    res = requests.get(url).json()

    return [
        f["properties"].get("name")
        for f in res.get("features", [])
        if f["properties"].get("name")
    ]