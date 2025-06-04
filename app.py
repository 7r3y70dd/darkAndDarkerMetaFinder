from flask import Flask
from models import db                        # ← reuse the one defined in models
from routes import bp as main_bp             # blueprint with all routes

def create_app() -> Flask:
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')
    app.config.update(
        SQLALCHEMY_DATABASE_URI='sqlite:///dark_darker.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)                         # bind SQLAlchemy

    app.register_blueprint(main_bp)          # add routes

    # create tables the first time the app runs
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    # `flask run` also works once FLASK_APP is set, but this
    # lets you just `python app.py` while experimenting.
    create_app().run(debug=True)

