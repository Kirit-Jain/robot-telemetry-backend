from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any

class TelemetryCreate(BaseModel):
    robot_id: str
    location: Dict[str, float]
    battery_level: float | None = None

class Telemetry(TelemetryCreate):
    id: int
    timestamp: datetime

class Config:
    from_attributes = True