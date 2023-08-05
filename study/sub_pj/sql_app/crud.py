from sqlalchemy.orm import Session
from . import models, schemas
import sql_app.database


# import sql_app.models # 절대경로로 불러오는방법
# import sql_app.schemas # 절대경로로 불러오는방법

def get_state(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stock).offset(skip).limit(limit).all()