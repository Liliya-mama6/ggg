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
async def create(username:str=Path(min_length=5, max_length=20, description='Enter username', example='urban'),
                 age:int=Path(ge=18, le=120, description='EnterUSER age', example='22')) -> str:
    a=str(int(max(users, key=int))+1)
    users[a]=f"Имя: {str(username)}, возраст: {str(age)}"
    return f"User {a} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update(user_id:int = Path(ge=1, le=100, description='EnterUSER id', example='12'),
                 username:str=Path(min_length=5, max_length=20, description='Enter username', example='urban'),
                 age:int=Path(ge=18, le=120, description='Enter age', example='119')) ->str:
    users[user_id]=f'Имя: {str(username)}, возраст: {str(age)}'
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete(user_id:int=Path(ge=1, le=100, description='EnterUSER id', example='12'))->str:
    users.pop(user_id)
    return f'The user {user_id} was deleted'
