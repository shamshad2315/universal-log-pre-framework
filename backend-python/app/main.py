from fastapi import FastAPI

from app.api.routes import router
from app.core.database import Base, engine
from app.models.event import Event


app = FastAPI(title="ULPF Backend")


# Create database tables
Base.metadata.create_all(bind=engine)


# Register API routes
app.include_router(router)