from fastapi import FastAPI
from app.db.database import engine
from app.db import models
from app.routes import auth_routes

# DROP old tables (dangerous if you have data!)
models.Base.metadata.drop_all(bind=engine)

# CREATE new tables from your current models
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SME Business Management API",
    version="1.0.0",
)

app.include_router(auth_routes.router)

@app.get('/')
def read_root():
    return {"message": "SME API is running successfully!"}