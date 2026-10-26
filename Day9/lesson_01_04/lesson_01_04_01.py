# FASTAPI
# Create POST    statuse 201
# Rread  GET
# Update PUT/PATCH
# Delete DELETE

# 초기데이터 list[dic]
# dict --> id:int(1이상), name : str (1글자이상), massage : str (1글자이상)

# tasks = [
#     {'id':1, 'name':'홍길동', messge':'동해번쩍'}
# ]

# tasks = []


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# 초기 데이터
tasks = []


# 데이터 입력 조건
class TaskCreate(BaseModel):
    title: str = Field(min_length=1)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    done: bool | None = None


# 다음 ID 생성
def next_id():
    return max((task["id"] for task in tasks), default=0) + 1


# 특정 할 일 찾기
def find_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# 1. 전체 할 일 조회
@app.get("/tasks")
def get_tasks():
    return tasks


# 2. 특정 할 일 조회
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return find_task(task_id)


# 3. 할 일 추가
@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate):
    new_task = {
        "id": next_id(),
        "title": payload.title,
        "done": False
    }

    tasks.append(new_task)
    return new_task


# 4. 할 일 수정
@app.patch("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskUpdate):
    task = find_task(task_id)
    updates = payload.model_dump(exclude_unset=True)
    task.update(updates)
    return task


# 5. 할 일 삭제
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")
