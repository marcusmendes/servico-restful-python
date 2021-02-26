from app.database.base import Base, engine


def create_table():
    Base.metadata.create_all(engine)
