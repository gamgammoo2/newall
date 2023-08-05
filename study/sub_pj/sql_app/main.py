from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session, sessionmaker

import sqlalchemy.orm.session

import sql_app.models
import sql_app.database
import sql_app.schemas
import sql_app.crud


sql_app.models.Base.metadata.create_all(bind=sql_app.database.engine)

app = FastAPI()


# Dependency
def get_db():
    db = sql_app.database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/select", response_model=List[schemas.Stock])
def select_state(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    state = crud.get_state(db, skip=skip, limit=limit)
    return state