from typing import List, Optional

from pydantic import BaseModel # 객체 타입설정


class StockBase(BaseModel):
    title: str
    description: Optional[str] = None


class StockCreate(StockBase):
    pass


class Stock(StockBase):
    Code : int

    class Config:
        orm_mode = True


