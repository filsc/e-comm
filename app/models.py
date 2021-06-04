from flask_login import UserMixin
from app import db, login
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def generate_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 


    def from_dict(self, data):
       for attr in ['email', 'password']:
           if attr in data:
               if attr =='email':
                   setattr(self, attr, data[attr].lower())

@login.user_loader
def get_user(id):
    return User.query.get(int(id))