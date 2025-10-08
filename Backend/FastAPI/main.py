from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI"

## Para iniciar un servidor uvicorn usamos: uvicorn main:app --reload (Tiene que estar en el directorio y los nombres correctos)
# o usar fastapi dev main.py (recomendado) y para salir control + c

@app.get("/url")
async def url():
    return { "url": "https://mouredev.com/python" }

## FastAPI a medidad que vas programando, se va generando documentación en /docs
