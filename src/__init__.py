import json
from .config import DBConnection
from .entities import Users as UsersModel


class UserRepo:
    '''Users model repository'''

    def insert_user(self, name: str):
        '''Insert user in db method'''

        with DBConnection() as db:
            new_user = UsersModel(name=name)
            db.session.add(new_user)
            db.session.commit()

    def list_users(self):
        '''List users in db method'''

        with DBConnection() as db:
            users = db.session.query(UsersModel).all()

            formatted_users = json.dumps([user.to_json() for user in users])

            return formatted_users
