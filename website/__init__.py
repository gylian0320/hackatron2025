from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin


login_manager = LoginManager()
login_manager.login_view = "auth.login"

db = SQLAlchemy()

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

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///User.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app