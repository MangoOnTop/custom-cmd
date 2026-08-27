import requests

def weather(city: str) -> str:
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        return response.text
    except Exception:
        return "Could not fetch weather"