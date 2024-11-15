import fastapi
app=fastapi.FastAPI()

#$ python3 -m uvicorn fgfg:app
@app.get('/')
async def welkome()->str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin()->str:
    return "Вы вошли как администратор"


@app.get('/user/{userid}')
async def iduser(userid)->str:
    return f"Вы вошли как пользователь № {userid}"


@app.get('/user')
async def iduser(name:str='anonim', age : int=25)->str:
    return f"Информация о пользователе. Имя: {name}, Возраст: {age}"
