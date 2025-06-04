from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()                            # exported for reuse


# populate_db.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///game.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Classes(db.Model):
    """
    Minimal illustration: just the base-attribute table.
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

    def __repr__(self) -> str:
        return f"<Class {self.name}>"

class Perk(db.Model):
    __tablename__ = "perks"

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), unique=True, nullable=False)
    class_name = db.Column(db.String(50), nullable=False)  # new column
    bonuses    = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Perk {self.name} for {self.class_name}>"

class Skill(db.Model):
    __tablename__ = "skills"

    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(100), unique=True, nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    bonuses  = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Skill {self.name}>"

class Spell(db.Model):
    __tablename__ = "spells"

    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(100), unique=True, nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    bonuses  = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Spell {self.name}>"

class Weapon(db.Model):
    __tablename__ = "weapons"

    id                = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50), nullable=False, default=list)
    name              = db.Column(db.String(100), unique=True, nullable=False)
    damage            = db.Column(db.String(50), nullable=False)
    static_attributes = db.Column(db.JSON, default=list)
    rarity            = db.Column(db.String(50), nullable=False)
    bonuses           = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Weapon {self.name}>"

class Helmet(db.Model):
    __tablename__ = "helmets"

    id                = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50), nullable=False, default=list)
    name              = db.Column(db.String(100), unique=True, nullable=False)
    armor_rating      = db.Column(db.Integer, nullable=False)
    rarity            = db.Column(db.String(50), nullable=False)
    static_attributes = db.Column(db.JSON, default=list)
    bonuses           = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Helmet {self.name}>"

class Chestpiece(db.Model):
    __tablename__ = "chestpieces"

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(100), unique=True, nullable=False)
    armor_rating      = db.Column(db.Integer, nullable=False)
    rarity            = db.Column(db.String(50), nullable=False)
    static_attributes = db.Column(db.JSON, default=list)
    class_name = db.Column(db.String(50), nullable=False, default=list)
    bonuses           = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Chestpiece {self.name}>"

class Pants(db.Model):
    __tablename__ = "pants"

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(100), unique=True, nullable=False)
    armor_rating      = db.Column(db.Integer, nullable=False)
    rarity            = db.Column(db.String(50), nullable=False)
    static_attributes = db.Column(db.JSON, default=list)
    class_name = db.Column(db.String(50), nullable=False, default=list)
    bonuses           = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Pants {self.name}>"

class Boots(db.Model):
    __tablename__ = "boots"

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(100), unique=True, nullable=False)
    armor_rating      = db.Column(db.Integer, nullable=False)
    rarity            = db.Column(db.String(50), nullable=False)
    static_attributes = db.Column(db.JSON, default=list)
    bonuses           = db.Column(db.JSON, default=list)
    class_name = db.Column(db.String(50), nullable=False, default=list)

    def __repr__(self) -> str:
        return f"<Boots {self.name}>"

class Gloves(db.Model):
    __tablename__ = "gloves"

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(100), unique=True, nullable=False)
    armor_rating      = db.Column(db.Integer, nullable=False)
    rarity            = db.Column(db.String(50), nullable=False)
    static_attributes = db.Column(db.JSON, default=list)
    bonuses           = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Gloves {self.name}>"

class Item(db.Model):
    __tablename__ = "items"

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100), unique=True, nullable=False)
    bonuses = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Item {self.name}>"

class Cape(db.Model):
    __tablename__ = "capes"

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100), unique=True, nullable=False)
    bonuses = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Cape {self.name}>"

class Necklace(db.Model):
    __tablename__ = "necklaces"

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(100), unique=True, nullable=False)
    static_attributes = db.Column(db.JSON, default=list)
    bonuses           = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Necklace {self.name}>"

class Ring(db.Model):
    __tablename__ = "rings"

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(100), unique=True, nullable=False)
    static_attributes = db.Column(db.JSON, default=list)
    bonuses           = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Ring {self.name}>"

class Bonus(db.Model):
    __tablename__ = "bonuses"

    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(100), nullable=False)
    max_roll  = db.Column(db.Integer, nullable=False)
    is_unique = db.Column(db.Boolean, unique=True, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<Bonus {self.name} (max_roll={self.max_roll}, unique={self.is_unique})>"
