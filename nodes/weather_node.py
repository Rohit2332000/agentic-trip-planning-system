from services.weather import get_weather

def weather_node(state):
    forecast = get_weather(state["city"])

    return {
        "weather_forecast": forecast,
        "weather_summary": forecast[0]["condition"] if forecast else "N/A"
    }