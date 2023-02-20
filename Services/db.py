from Database.database import Base, engine, SessionLocal


def create_database():
    return Base.metadata.create_all(bind=engine)


class LibrayManagment:
    def __init__(self):
        self.db = get_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
