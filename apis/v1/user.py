from app.models import User, NCUser
from random import randint
from app import response, validator
from datetime import datetime

def register(data):
    if not validator(section='register', data=data):
        return response(message='invalid_params', error=True, code=400)
    if NCUser.query.filter_by(phone=data['phone']).first():
        return response(message='not_confirmed_user', error=True)
    if User.query.filter_by(phone=data['phone']).first():
        return response(message='user_exists', error=True)
    new_user = NCUser(phone = data['phone'])
    new_user.confirm_code = randint(1000, 9999)
    new_user.name = data['name']
    new_user.surname = data['surname']
    new_user.attempts = {}
    new_user.last_attempt = {}
    if new_user.save(): return response(message='code_is_sent')
    return response(error=True, message='unknown_error')