import fastapi
from pydantic import BaseModel
from fastapi import Path, HTTPException, Body
from typing import List

app = fastapi.FastAPI()

# $ python3 -m uvicorn iscandar:app
users = []
a=0


class User(BaseModel):
    id: int = None
    nick: str
    year: int


@app.get('/')
async def welcome() -> str:
    return 'welcome to my sait'


@app.get('/users')
async def get() -> List[User]:
    return users


@app.post(path='/user/{username}/{age}')
async def create(username: str, age: int) -> User:
    a=max(i.id for i in users)
    user: User = User(id=a, nick=username, year=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update(user_id, username, age) -> User:
    try:
        for i in users:
            if i.id==user_id:
                i.nick=username
                i.year=age
                return i
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete(user_id) -> str:
    global users
    try:
        c=0
        for i in users:
            if i.id==user_id:
                del users[c]
                return 'user was deleted'
            c+=1
    except:
        HTTPException(status_code=404, detail="User was not found")

