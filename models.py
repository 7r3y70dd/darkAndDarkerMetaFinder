from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()                            # exported for reuse


class Classes(db.Model):
    """
    Minimal illustration: just the base-attribute table.
    Add other tables (Items, Enchantments, …) the same way.
    """
    __tablename__ = "classes"

    id               = db.Column(db.Integer, primary_key=True)
    name             = db.Column(db.String(50), unique=True, nullable=False)
    strength         = db.Column(db.Integer, default=0)
    vigor            = db.Column(db.Integer, default=0)
    agility          = db.Column(db.Integer, default=0)
    dexterity        = db.Column(db.Integer, default=0)
    will             = db.Column(db.Integer, default=0)
    knowledge        = db.Column(db.Integer, default=0)
    resourcefulness  = db.Column(db.Integer, default=0)
    base_hp          = db.Column(db.Float,   default=0)

    def __repr__(self) -> str:               # helpful in shell/debugger
        return f"<Class {self.name}>"

