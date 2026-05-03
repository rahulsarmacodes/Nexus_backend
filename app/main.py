from fastapi import FastAPI
from app.db.base import Base
from app.db.database import engine
from app.api.routes import router as portfolio_router
app = FastAPI()

app.include_router(portfolio_router)

#create tables
Base.metadata.create_all(bind = engine)