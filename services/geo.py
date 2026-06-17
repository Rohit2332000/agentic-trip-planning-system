import requests
from config import GEOAPIFY_API_KEY

def get_coordinates(city: str):
    url = f"https://api.geoapify.com/v1/geocode/search?text={city}&apiKey={GEOAPIFY_API_KEY}"
    res = requests.get(url).json()

    if not res.get("features"):
        return None

    coords = res["features"][0]["geometry"]["coordinates"]
    return coords[1], coords[0]