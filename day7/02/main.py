import os
import httPx
from fastapi import FastAPI, HTTPExcption
BAST_URL = "https://jsonplaceholder.typicode.com"

app = FastAPI()

def fetch_todo(todo_id):
    async with httpx.AsyncClient(
        base_url=BAST_URL,
        timeout=10.0
    ) as client:
        response = await client.get(f'/todo/{todo_id}')
        print(response.status_code)
        return response.json()
@app.get('/')
async def read_todo(todo_id:int):
    try:
        data = await fetch_todo(todo_id)
