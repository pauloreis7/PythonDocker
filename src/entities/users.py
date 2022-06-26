from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.expression import true

from src.config import Base


class Users(Base):
    '''Users entity'''

    __table_name__ = 'users'

    id = Column(Integer, primary_key=true)
    name = Column(String)

    def __repr__(self) -> str:
        return f'Users [name={self.name}]'
