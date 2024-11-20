import fastapi
from fastapi import Path
from typing import Annotated
app=fastapi.FastAPI()

#$ python3 -m uvicorn fgfg:app
@app.get('/')
async def welkome()->str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin()->str:
    return "Вы вошли как администратор"


@app.get('/user/{userid}')
async def iduser(userid:int=Path(ge=1, le=100, description='EnterUSER ID', example='12'))->str:
    return f"Вы вошли как пользователь № {userid}"


@app.get('/user/{username}/{age}')
async def idser(username:str=Path(min_length=5, max_length=20, description='Enter username', example='urban'),
                age : int=Path(ge=18, le=120, description='Enter age', example='119'))->str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
