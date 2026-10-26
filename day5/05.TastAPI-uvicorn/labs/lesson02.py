from fastapi import FastAPI

app = FastAPI(title="Lesson 02")

@app.get("/method")
def read_method():
    return {"method": "GET", "purpose": "read"}

#swagger UI에서 post 요청을 테스트할 수 있도록 status_code=201을 추가
@app.post("/method", status_code=201) #create
def create_method():
    return {"method": "POST", "purpose": "create"}