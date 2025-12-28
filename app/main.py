from fastapi import FastAPI
from app.db.session import engine
from app.db.models import Base

app = FastAPI(title="Kasparro Backend System")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}
