from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
import models.users
from database import get_db, engine

app = FastAPI()
models.users.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/users/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.users.User).all()
    return {"message": users}