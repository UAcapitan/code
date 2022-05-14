from typing import List
from pydantic import BaseModel, validator, Field
from datetime import date

class Genre(BaseModel):
    name: str

class Book(BaseModel):
    title: str = Field(..., max_length=25)
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int
    count: int = Field(
        ...,
        gt=15,
        lt=90,
        description='Author age must be more than 15 and less than 90'
    )

    @validator('pages')
    def check_pages(cls, v):
        if v < 50:
            raise ValueError('Pages of book must be more than 50')
        return 50

class BookOut(Book):
    id: int