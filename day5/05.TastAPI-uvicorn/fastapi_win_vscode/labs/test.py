tasks = [{1, {'id':1, "title": "FastAPI basics", "done": False}}]

# 1. 데이터 조회 get(/tacks)
# return tasks

# 2. 데이터 추가 post(/tacks)
# tasks.append({"id": 2, "title": FastAPI advanced", "done" : False}})
              
# 3. 특정번호의 데이터 조회 get(/tacks/{task_id})
# retrn tasks[task_id]

# 4. 특정번호의 데이터를 전부교체 put(/tacks/{task_id})
# tasks[task_id] = {"id": task_id, "title": "FastAPI advanced", "done" : False}   

# 5. 특정번호의 데이터 일부 수정 patch(/tacks/{task_id})