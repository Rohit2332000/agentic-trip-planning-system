from tavily import TavilyClient
from config import TAVILY_API_KEY

tavily = TavilyClient(api_key=TAVILY_API_KEY)

def get_attractions(city: str):
    res = tavily.search(query=f"top attractions in {city}", max_results=5)
    return [r["content"] for r in res["results"]]