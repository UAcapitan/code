from typing import List
from pydantic import BaseModel, validator
from datetime import date

class Genre(BaseModel):
    name: str

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int

    @validator('pages')
    def check_pages(cls, v):
        if v < 50:
            raise ValueError('Pages of book must be more than 50')
        return 50