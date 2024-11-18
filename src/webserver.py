from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from paho.mqtt.client import MQTTMessage, Client



# Wenn das Internet das Web ist, dann bin ich die Spinne!
app = FastAPI()


# http://127.0.0.1:8000/light/1?state=on
@app.post("/light/{light_id}")
def light(light_id: int, state: Union[str, None] = None):
    print(f"{light_id=}, {state=}")
    client = Client()
    # client.publish()
    # mosq.publish(f'/fiv/lb/{state.id}/state', state.enabled, 0)
    # return { "light_id": light_id, "state": state }


app.mount("/", StaticFiles(directory="ui", html=True), name="ui")
