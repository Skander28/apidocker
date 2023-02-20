from typing import List
from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from Exception.exception import AuthorNotFound, AuthorExisted, NoBooks, BookNotFound
from Models.schema import BookM, AuthorM
from Services.db import get_db
from Services.Crud import add_book_service, add_author_service, get_book_service, delete_book_service, \
    update_book_service, get_books_service

route = APIRouter()


@route.post("/add-book/", response_model=BookM)
async def add_book(book: BookM, db: Session = Depends(get_db)):
    try:
        return await add_book_service(book=book, db=db)
    except AuthorNotFound as not_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=not_found.message)


@route.post("/add-author/", response_model=AuthorM)
async def add_author(author: AuthorM, db: Session = Depends(get_db)):
    try:
        return await add_author_service(author=author, db=db)
    except AuthorExisted as exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exist.message)


@route.get("/books/", response_model=List[BookM])
async def get_books(db: Session = Depends(get_db)):
    try:
        return await get_books_service(db=db)
    except NoBooks as empty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=empty.message)


@route.get("/books/{book_id}", response_model=BookM)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    try:
        book = await get_book_service(book_id=book_id, db=db)
        return book
    except BookNotFound as not_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=not_found.message)


@route.delete("/books/{Book_id}", response_model=BookM)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    try:
        book = await get_book_service(book_id=book_id, db=db)
        await delete_book_service(book, db=db)
        return "successfully deleted the book"
    except BookNotFound as not_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=not_found.message)


@route.put("/books/{book_id}", response_model=BookM)
async def update_book(book_id: int, book_data: BookM, db: Session = Depends(get_db)):
    try:
        book = await get_book_service(book_id=book_id, db=db)
        return await update_book_service(book_data=book_data, book=book, db=db)
    except BookNotFound as not_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=not_found.message)

