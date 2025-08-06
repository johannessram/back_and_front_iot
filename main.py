from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Stockage temporaire en mémoire
latest_distance: Optional[float] = None

# Modèle des données envoyées par ESP32
class DistanceData(BaseModel):
    distance: float

# Route pour recevoir les données de l'ESP32 (POST)
@app.post("/send-distance")
async def receive_distance(data: DistanceData):
    global latest_distance
    latest_distance = data.distance
    return {"message": "Distance received successfully", "distance": latest_distance}

# Route pour consulter la dernière distance reçue (GET)
@app.get("/get-distance")
async def get_distance():
    if latest_distance is None:
        return {"message": "No distance received yet"}
    return {"distance": latest_distance}
