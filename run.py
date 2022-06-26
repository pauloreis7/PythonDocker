from flask import Flask, request, jsonify

from src import UserRepo

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    '''flask check function'''

    return 'Hello Flask'


@app.route('/users/insert', methods=['POST'])
def insert_user():
    '''Insert user in db route'''

    user_repo = UserRepo()
    request_body = request.json

    user_repo.insert_user(request_body['name'])

    return jsonify({'msg': 'user created!'})


@app.route('/users/list', methods=['GET'])
def list_users():
    '''List db users'''

    user_repo = UserRepo()

    users = user_repo.list_users()

    return jsonify(users)
