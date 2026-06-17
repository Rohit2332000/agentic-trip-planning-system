import requests
from config import ORS_API_KEY

def get_route(source, destination):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    body = {"coordinates": [list(source), list(destination)]}

    headers = {"Authorization": ORS_API_KEY}

    res = requests.post(url, json=body, headers=headers).json()

    summary = res["routes"][0]["summary"]

    return (
        summary["distance"] / 1000,
        summary["duration"] / 3600
    )