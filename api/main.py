from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import time

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Robot Telemetry API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#--- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Robot Telemetry API"}

@app.post("/telemetry/", response_model=schemas.Telemetry)
def create_telemetry(
    telemetry: schemas.TelemetryCreate,
    db: Session = Depends(get_db)
):
    """
    Receive a new telemetry data point and save it to the database.
    """
    return crud.create_telemetry_entry(db=db, telemetry=telemetry)

@app.get("/telemetry/{robot_id}", response_model=List[schemas.Telemetry])
def read_telemetry_for_robot(
    robot_id: str,
    skip: int=0,
    limit: int=100,
    db: Session=Depends(get_db)
):
    """
    Retrive all telemetry data points for a specific robot.
    """
    entries = crud.get_telemetry_by_robot(db, robot_id=robot_id, skip=skip, limit=limit)
    if not entries:
        pass
    return entries
