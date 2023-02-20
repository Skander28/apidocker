from pydantic import BaseModel


class BookM(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True


class AuthorM(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True
