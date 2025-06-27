from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from collections import deque
from datetime import datetime

app = FastAPI()

# --- Models ---
class StatusUpdate(BaseModel):
    step: str
    detail: Optional[str] = None

class StatusItem(BaseModel):
    timestamp: str
    step: str
    detail: str

# --- Queue for status history ---
status_queue = deque(maxlen=100)  # store latest 100 updates

@app.post("/update_status")
def update_status(update: StatusUpdate):
    status_item = StatusItem(
        timestamp=datetime.now().isoformat(timespec='seconds'),
        step=update.step,
        detail=update.detail or ""
    )
    status_queue.append(status_item)
    return {"message": "Status queued"}

@app.get("/status/latest")
def get_latest_status():
    if not status_queue:
        return {"step": "Idle", "detail": "", "timestamp": ""}
    latest = status_queue[-1]
    return latest

@app.get("/status/history")
def get_status_history() -> List[StatusItem]:
    return list(status_queue)
