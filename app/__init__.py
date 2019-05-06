from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.ext import mutable

from instance.config import app_config

db = SQLAlchemy(session_options={'autocommit': True})

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app

def response(error = False, message = '', data = {}, code = 200):
    return {
        'status': 'success' if not error else 'error',
        'message': message,
        'data': data
    }, code

def maxmin(data, min, max):
    return len(data) > min and len(data) < max

def validator(data, section = 'other'):
    valid = True
    if section == 'other':
        return valid
    elif section == 'register':
        for i in ['phone', 'name', 'surname']:
            valid = valid and data.get(i)
        valid = valid and len(data['phone']) == 9 and maxmin(data['name'], 2, 15) and maxmin(data['surname'], 5, 35)
    return valid

class BaseModel():
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class JsonEncodedDict(db.TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)


mutable.MutableDict.associate_with(JsonEncodedDict)