import fastapi
from pydantic import BaseModel
from fastapi import Path,  HTTPException, Body
from typing import List

app = fastapi.FastAPI()

# $ python3 -m uvicorn iscandar:app
users = []


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
async def create(username:str, age:int) -> User:
    user:User = User(id=len(users)+1, nick=username, year=age)
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update(user_id, username, age) -> str:
    try:
        a=users[user_id]
        a.nick=username
        a.year=age
        users[user_id]=a
        return 'all was successful'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
    

@app.delete('/user/{user_id}')
async def delete(user_id) -> str:
    global users
    try:
        new_users=users[:user_id]+users[user_id+1:]
        users=new_users
        return 'User was deleted'
    except:
        HTTPException(status_code=404, detail="User was not found")
