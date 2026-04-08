from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from app.controllers.user_controller import router as user_router
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = FastAPI(title="FastAPI MVC MongoDB")

# Static files (CSS, JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# Templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env = Environment(
    loader=FileSystemLoader(os.path.join(BASE_DIR, "templates")),
    autoescape=select_autoescape(["html", "xml"]),
    cache_size=0   # 🚨 DISABLE CACHE (this fixes your error)
)
templates = Jinja2Templates(env=env)

app.include_router(user_router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request}
    )