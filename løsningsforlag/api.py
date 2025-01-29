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

@app.post("/")
async def get_joke(id: str | None = "zkO7wHJmrc"):
    headers = {'Accept': 'application/json'}
    response = requests.get('https://icanhazdadjoke.com/j/' + id , headers=headers)
    data = response.json()
    return data["joke"]