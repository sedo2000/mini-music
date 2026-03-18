from fastapi import APIRouter
from .db import load_tracks

router = APIRouter()


@router.get("/tracks")
def list_tracks():
    return load_tracks()


@router.get("/stream/{track_id}")
def stream_track(track_id: int):
    tracks = load_tracks()
    for t in tracks:
        if t["id"] == track_id:
            return {"url": t["file"]}
    return {"error": "Track not found"}
