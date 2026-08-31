import json

from fastapi import APIRouter
from pydantic import BaseModel

from app.parsers.registry import get_parser
from app.core.logger import get_logger
from app.core.database import SessionLocal
from app.models.event import Event


router = APIRouter()
logger = get_logger("ULPF")


class LogRequest(BaseModel):
    parser: str
    log: str


@router.get("/")
def home():
    return {"message": "ULPF Backend is running"}


@router.post("/parse")
def parse_log(request: LogRequest):
    logger.info(f"Log received | parser={request.parser}")

    parser = get_parser(request.parser)

    logger.info(f"Parser selected | parser={request.parser}")

    result = parser.parse(request.log)

    logger.info(f"Log parsed successfully | parser={request.parser}")

    if "error" not in result:
        db = SessionLocal()

        try:
            event = Event(
                parser=result.get("parser"),
                event=result.get("event"),
                timestamp=result.get("timestamp"),
                host=result.get("host"),
                vendor=result.get("vendor"),
                product=result.get("product"),
                user=result.get("user"),
                source_ip=result.get("source_ip"),
                destination_ip=result.get("destination_ip"),
                severity=result.get("severity"),
                data=json.dumps(result.get("data", {}))
            )

            db.add(event)
            db.commit()
            db.refresh(event)

            logger.info(
                f"Event saved to database | id={event.id} | parser={request.parser}"
            )

        finally:
            db.close()

    return result


@router.get("/events")
def get_events():
    db = SessionLocal()

    try:
        events = db.query(Event).all()

        return [
            {
                "id": event.id,
                "parser": event.parser,
                "event": event.event,
                "timestamp": event.timestamp,
                "host": event.host,
                "vendor": event.vendor,
                "product": event.product,
                "user": event.user,
                "source_ip": event.source_ip,
                "destination_ip": event.destination_ip,
                "severity": event.severity,
                "data": event.data
            }
            for event in events
        ]

    finally:
        db.close()