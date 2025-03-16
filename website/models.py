from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    birthday = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        lst = []
        lst.append(f"ID={self.id}")
        lst.append(f"First Name={self.first_name}")
        lst.append(f"Last Name={self.last_name}")
        lst.append(f"Birthday={self.birthday}")
        lst.append(f"Gender={self.gender}")
        lst.append(f"Email={self.email}")
        lst.append(f"Password={self.password}")
        return "\n".join(lst)
