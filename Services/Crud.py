from typing import List

from Exception.exception import AuthorExisted, AuthorNotFound, NoBooks, BookNotFound
from Models.models import Book, Author
from Models.schema import BookM, AuthorM


async def add_book_service(book: BookM, db: "Session") -> BookM:
    try:
        db_book = Book(title=book.title, rating=book.rating, author_id=book.author_id)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
    except Exception as error:
        raise AuthorNotFound

    return BookM.from_orm(db_book)


async def add_author_service(author: AuthorM, db: "Session") -> AuthorM:
    try:
        db_author = Author(name=author.name, age=author.age)
        db.add(db_author)
        db.commit()
        db.refresh(db_author)
    except Exception as error:
        raise AuthorExisted


async def get_books_service(db: "Session") -> List[BookM]:
    try:
        books = db.query(Book).all()
        return list(map(BookM.from_orm, books))
    except Exception as error:
        raise NoBooks


async def get_book_service(book_id: int, db: "Session"):
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        return book
    except Exception as error:
        raise BookNotFound


async def delete_book_service(book: Book, db: "Session"):
    try:
        db.delete(book)
        db.commit()
    except Exception as error:
        raise BookNotFound


async def update_book_service(book_data: BookM, book: Book, db: "Session") -> BookM:
    try:
        book.title = book_data.title
        book.rating = book_data.rating
        book.author_id = book_data.author_id

        db.commit()
        db.refresh(book)

        return BookM.from_orm(book)
    except Exception as error:
        raise BookNotFound
