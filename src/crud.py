from fastapi import *
from fastapi.middleware.cors import *
from pydantic import *
from typing import *
import time

app = FastAPI(title="TODO")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # В продакшене заменить на реальный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskCreate(BaseModel):
    text: str

class Task(BaseModel):
    id: str
    text: str

tasks_db = [
    Task(id="1", text="Почитать книгу"),
    Task(id="2", text="Сходить в спортзал")
]

@app.get("/tasks", response_model=List[Task])
async def getTasks() -> List[Task]:
    return tasks_db

@app.post("/tasks", response_model=Task, status_code=201)
async def createTask(task: TaskCreate) -> Task:
    new_id = str(int(time.time() * 1000))
    new_task = Task(id=new_id, text=task.text)
    tasks_db.append(new_task)
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
async def getTask(task_id: str) -> Task:
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.delete("/tasks", status_code=200)
async def deleteAllTasks() -> Dict:
    tasks_db.clear()
    return {"detail": "Все задачи удалены"}

@app.delete("/tasks/{task_id}", status_code=200)
async def deleteTask(task_id: str) -> Dict:
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return {"detail": f"Задача с ID={task_id} удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")
