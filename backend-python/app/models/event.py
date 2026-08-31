from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    parser = Column(String, nullable=False)
    event = Column(String, nullable=True)
    timestamp = Column(String, nullable=True)
    host = Column(String, nullable=True)
    vendor = Column(String, nullable=True)
    product = Column(String, nullable=True)
    user = Column(String, nullable=True)

    source_ip = Column(String, nullable=True)
    destination_ip = Column(String, nullable=True)
    severity = Column(String, nullable=True)

    data = Column(Text, nullable=True)