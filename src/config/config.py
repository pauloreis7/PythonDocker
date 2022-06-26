from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnection:
    '''DB SQL connection sqlalchemy class'''

    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:mypass@mysqldb/test'
        self.session = None

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()

        self.session = session_maker(bind=engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
