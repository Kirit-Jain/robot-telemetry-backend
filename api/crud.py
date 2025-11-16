from sqlalchemy.orm import Session
import models, schemas

def create_telemetry_entry(db: Session, telemetry: schemas.TelemetryCreate):
    """
    Create a new telemetry entry in the database.
    """

    db_telemetry = models.Telemetry(
        robot_id=telemetry.robot_id,
        location=telemetry.location,
        battery_level=telemetry.battery_level
    )

    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    return db_telemetry

def get_telemetry_by_robot(db: Session, robot_id: str, skip: int=0, limit: int=100):
    """
    Get all telemetry entries for a specific robot
    """

    return db.query(models.Telemetry).filter(models.Telemetry.robot_id == robot_id).offset(skip).limit(limit).all()