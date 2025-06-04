from flask import Blueprint, render_template
from models import Classes

bp = Blueprint("main", __name__)             # `url_prefix` optional


@bp.route("/")
def home():
    classes = Classes.query.all()            # grab every row
    return render_template("home.html",
                           title="Home",
                           classes=classes)

