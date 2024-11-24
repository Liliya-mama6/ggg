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
    global a
    a+=1
    user: User = User(id=a, nick=username, year=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update(user_id, username, age) -> str:
    try:
        a:User=User(id=user_id, nick=username, year=age)
        users[user_id] = a
        return 'all was successful'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete(user_id) -> str:
    global users
    try:
        new_users = users[:user_id - 1] + users[user_id:]
        users = new_users
        return 'User was deleted'
    except:
        HTTPException(status_code=404, detail="User was not found")

