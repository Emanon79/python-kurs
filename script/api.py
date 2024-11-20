import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_joke():
    headers = {'Accept': 'application/json'}
    r = requests.get('https://icanhazdadjoke.com/', headers=headers)
    d = r.json()
    return(d["joke"])



