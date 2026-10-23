from fastapi import FastAPI

app = FastAPI(title="Lesson 01")

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

@app.get("/sports")
def sports():
    return {"sports": ["soccer", "basketball", "tennis", "baseball"]}