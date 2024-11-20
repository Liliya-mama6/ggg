import fastapi
from fastapi import Path
from typing import Annotated
app=fastapi.FastAPI()

#$ python3 -m uvicorn fgfg:app
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create(username, age) -> str:
    a=str(int(max(users, key=int))+1)
    users[a]=f"Имя: {str(username)}, возраст: {str(age)}"
    return f"User {a} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update(user_id, username, age) ->str:
    users[user_id]=f'Имя: {str(username)}, возраст: {str(age)}'
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete(user_id)->str:
    users.pop(user_id)
    return f'The user {user_id} was deleted'
