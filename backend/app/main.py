from fastapi import FastAPI
from app.db.database import engine
from app.db import models
from app.routes import auth_routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SME Business Management API",
    version="1.0.0",
)

app.include_router(auth_routes.router)

@app.get('/')
def read_root():
    return {"message": "SME API is running successfully!"}

import uvicorn
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)