from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sf6gg.models import Base


class DB:
    def __init__(self):
        self.session = None
        self.engine = None

    def init_engine(self, db_url: str):
        self.engine = create_engine(db_url, echo=True)
        self.session = sessionmaker(bind=self.engine)

    def init(self):
        if self.engine is None:
            raise
        Base.metadata.create_all(bind=self.engine)

    def get_session(self):
        if self.session is None:
            raise
        return self.session()


db = DB()
