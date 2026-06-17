from typing import TypedDict, List, Dict, Any, Optional

class TravelState(TypedDict):
    destination: str
    city: str
    source: str

    start_date: str
    end_date: str

    budget: str
    trip_type: str
    interests: List[str]

    overview: str
    attractions: List[str]
    restaurants: List[str]
    safety_tips: List[str]
    hotels: List[Dict[str, Any]]

    weather_summary: str
    weather_forecast: List[Dict[str, Any]]

    transportation: Dict[str, Any]
    itinerary: Dict[str, Any]

    formatted_itinerary: Optional[str]