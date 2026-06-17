import requests
from config import OPENWEATHER_API_KEY

def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"

    data = requests.get(url).json()

    forecast = []
    for item in data.get("list", [])[:6]:
        forecast.append({
            "time": item["dt_txt"],
            "temp": item["main"]["temp"],
            "condition": item["weather"][0]["description"]
        })

    return forecast