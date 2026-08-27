import requests

def joke() -> str:
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        return f"{data['setup']}\n{data['punchline']}"
    except Exception:
        return "Could not fetch joke"