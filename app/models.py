from app import db, BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(BaseModel, Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(15))
    name = db.Column(db.String(35), nullable=False)
    surname = db.Column(db.String(35), nullable=False)
    picture = db.Column(db.String(55), nullable=True)
    last_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, phone):
        self.phone = phone

    @staticmethod
    def get_all():
        return User.query.all()

    def __repr__(self):
        return "<User: {}>".format(self.phone)

class NCUser(BaseModel, db.Model):
    __tablename__ = 'nc_users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    confirm_code = db.Column(db.String(8), nullable=False)
    name = db.Column(db.String(35), nullable=False)
    surname = db.Column(db.String(35), nullable=False)
    attempts = db.Column(db.JSON)
    last_attempt = db.Column(db.JSON)

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, phone):
        self.phone = phone

    @staticmethod
    def get_all():
        return NCUser.query.all()

    def __repr__(self):
        return "<NCUser: {}>".format(self.phone)
