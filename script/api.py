import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_joke():
    """Get a random joke from the icanhazdadjoke API."""
    headers = {'Accept': 'application/json'}
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    data = response.json()
    return data["joke"]



