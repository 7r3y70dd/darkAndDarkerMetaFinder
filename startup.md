python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install Flask Flask-SQLAlchemy
export FLASK_APP=app:create_app  # Windows: set FLASK_APP=app:create_app
flask run

