import uvicorn
import socketio
from fastapi import FastAPI

app = FastAPI()

sio = socketio.AsyncServer(cors_allowed_origins=["*"], async_mode='asgi')

sio_app = socketio.ASGIApp(sio, socketio_path="/ws/socket.io")
app.mount("/ws", sio_app)


@sio.on("join_room")
async def handle_join_room_event(sid, data):
    print(sid, "{} has joined the room {}".format(data["username"], data["room"]))




if __name__=="__main__":
    uvicorn.run("sio:app")