from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
import starlette.status as status
from fastapi_socketio import SocketManager
from sockets import sio

app = FastAPI()
socket_manager = SocketManager(app=app)



templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})


@app.get("/chat", response_class=HTMLResponse)
async def signin(request: Request):
    return templates.TemplateResponse("chat.html", context={"request": request})


@app.post("/chat", response_class=RedirectResponse)
async def validate(request: Request):
    username = request.get("username")
    room = request.get("room")
    if username == username and room == room:
        return templates.TemplateResponse("chat.html", context={"request": request})
    else:
        redirect_url = request.url_for('home')
        return RedirectResponse(redirect_url, status_code=status.HTTP_302_FOUND)

