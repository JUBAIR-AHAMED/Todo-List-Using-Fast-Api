from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
app = FastAPI()

orgins=["localhost:3000",]

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    remove_todo,
    update_todo
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/todo/", response_model=list[Todo])
async def get_todo():
    response =await fetch_all_todos()
    if response:
        return response
    raise HTTPException(404,"No todos available")

@app.get("/api/todo{title}/", response_model=Todo)
async def get_todo_by_id(title):
    response=await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404,f"there is no todo with the title {title}")

@app.post("/api/todo{title}")
async def post_todo(todo: Todo):
    response = await create_todo(todo)
    if response:
        return response
    raise HTTPException(400,"Something went wrong")

@app.put("/api/put_todo{title}/")
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return "Successfully updated todo"
    raise HTTPException(404,f"there is no todo with the title {title}")


@app.delete("/api/delete_todo{title}/")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404,f"there is no todo with the title {title}")