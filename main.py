from fastapi import FastAPI 
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from tmdb_api import *


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def homepage():
    html_path = Path('static/index.html')
    return HTMLResponse(html_path.read_text())

@app.get("/movie")
async def movie(genre_id=None):
    data = get_movie(genre_id)
    return JSONResponse(data)

@app.get("/genre")
async def genre():
    data = get_genres()
    return JSONResponse(data)