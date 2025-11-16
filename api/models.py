from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from database import Base

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    robot_id = Column(String, index=True, nullable=False)

    location = Column(JSON)

    battery_level = Column(Float, nullable=True)

    timestamp = Column(DateTime(timezone=True), server_default=func.now())