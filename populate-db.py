# populate_db.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///game.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ─── Make sure there is exactly one `db` throughout this file ───
db = SQLAlchemy(app)


# ─── All models registered on the same `db` ─────────────────────────

class Classes(db.Model):
    """
    Minimal illustration: just the base‐attribute table.
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

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100), unique=True, nullable=False)
    bonuses = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Perk {self.name}>"


class Skill(db.Model):
    __tablename__ = "skills"

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100), unique=True, nullable=False)
    bonuses = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Skill {self.name}>"


class Spell(db.Model):
    __tablename__ = "spells"

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100), unique=True, nullable=False)
    bonuses = db.Column(db.JSON, default=list)

    def __repr__(self) -> str:
        return f"<Spell {self.name}>"


class Weapon(db.Model):
    __tablename__ = "weapons"

    id                = db.Column(db.Integer, primary_key=True)
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


# ─── Population logic ──────────────────────────────────────────────────────────

def populate():
    # 1) Create all tables (classes, perks, skills, spells, etc.)
    db.create_all()

    # ─── Insert one row into each table ────────────────────────────────────────

    # 1. Classes  ---------------------------------------------------------------
    Fighter = Classes(
        name="Fighter",
        strength=15,
        vigor=15,
        agility=15,
        dexterity=15,
        will=15,
        knowledge=15,
        resourcefulness=15,
        base_hp=110.0
    )
    db.session.add(Fighter)

    Barbarian = Classes(
        name="Barbarian",
        strength=25,
        vigor=25,
        agility=13,
        dexterity=12,
        will=18,
        knowledge=5,
        resourcefulness=7,
        base_hp=130.0
    )
    db.session.add(Barbarian)

    Rogue = Classes(
        name="Rogue",
        strength=9,
        vigor=10,
        agility=21,
        dexterity=25,
        will=10,
        knowledge=10,
        resourcefulness=20,
        base_hp=99.5
    )
    db.session.add(Rogue)

    Ranger = Classes(
        name="Ranger",
        strength=12,
        vigor=10,
        agility=20,
        dexterity=18,
        will=10,
        knowledge=12,
        resourcefulness=23,
        base_hp=101.0
    )
    db.session.add(Ranger)

    Wizard = Classes(
        name="Wizard",
        strength=6,
        vigor=7,
        agility=15,
        dexterity=17,
        will=20,
        knowledge=25,
        resourcefulness=15,
        base_hp=93.5
    )
    db.session.add(Wizard)

    Cleric = Classes(
        name="Cleric",
        strength=11,
        vigor=13,
        agility=12,
        dexterity=14,
        will=23,
        knowledge=20,
        resourcefulness=12,
        base_hp=105.0
    )
    db.session.add(Cleric)

    Bard = Classes(
        name="Bard",
        strength=13,
        vigor=13,
        agility=13,
        dexterity=20,
        will=11,
        knowledge=20,
        resourcefulness=15,
        base_hp=106.0
    )
    db.session.add(Bard)

    Warlock = Classes(
        name="Warlock",
        strength=11,
        vigor=14,
        agility=14,
        dexterity=15,
        will=22,
        knowledge=15,
        resourcefulness=14,
        base_hp=106.5
    )
    db.session.add(Warlock)

    Druid = Classes(
        name="Druid",
        strength=12,
        vigor=13,
        agility=12,
        dexterity=12,
        will=18,
        knowledge=20,
        resourcefulness=18,
        base_hp=105.5
    )
    db.session.add(Druid)

    Sorcerer = Classes(
        name="Sorcerer",
        strength=10,
        vigor=10,
        agility=10,
        dexterity=18,
        will=25,
        knowledge=20,
        resourcefulness=12,
        base_hp=100.0
    )
    db.session.add(Sorcerer)

    # finally, persist them
    db.session.commit()

    # 2. Perk
    perk = Perk(
        name="Steadfast",
        class_name="Warrior",
        bonuses=[{"type": "vigor", "value": 2}]
    )
    db.session.add(perk)

    # 3. Skill
    skill = Skill(
        name="Lockpicking",
        class_name="Rogue",
        bonuses=[{"type": "dexterity", "value": 3}]
    )
    db.session.add(skill)

    # 4. Spell
    spell = Spell(
        name="Fireball",
        class_name="Mage",
        bonuses=[{"type": "fire_damage", "value": 10}]
    )
    db.session.add(spell)

    # 5. Weapon
    weapon = Weapon(
        name="Longsword",
        class_name="Warrior",
        damage="1d8+2",
        static_attributes=["Versatile"],
        rarity="Rare",
        bonuses=[{"type": "strength", "value": 1}]
    )
    db.session.add(weapon)

    # 6. Helmet
    helmet = Helmet(
        name="Iron Helm",
        class_name="Warrior",
        armor_rating=5,
        rarity="Common",
        static_attributes=["Heavy"],
        bonuses=[{"type": "vigor", "value": 1}]
    )
    db.session.add(helmet)

    # 7. Chestpiece
    chestpiece = Chestpiece(
        name="Steel Cuirass",
        class_name="Warrior",
        armor_rating=10,
        rarity="Uncommon",
        static_attributes=["Sturdy"],
        bonuses=[{"type": "vigor", "value": 2}]
    )
    db.session.add(chestpiece)

    # 8. Pants
    pants = Pants(
        name="Leather Pants",
        class_name="Rogue",
        armor_rating=3,
        rarity="Common",
        static_attributes=["Lightweight"],
        bonuses=[{"type": "agility", "value": 1}]
    )
    db.session.add(pants)

    # 9. Boots
    boots = Boots(
        name="Traveler's Boots",
        class_name="Rogue",
        armor_rating=2,
        rarity="Common",
        static_attributes=["Comfortable"],
        bonuses=[{"type": "agility", "value": 1}]
    )
    db.session.add(boots)

    # 10. Gloves
    gloves = Gloves(
        name="Gauntlets",
        armor_rating=2,
        rarity="Uncommon",
        static_attributes=["Reinforced"],
        bonuses=[{"type": "strength", "value": 1}]
    )
    db.session.add(gloves)

    # 11. Item
    item = Item(
        name="Health Potion",
        bonuses=[{"type": "hp_restore", "value": 50}]
    )
    db.session.add(item)

    # 12. Cape
    cape = Cape(
        name="Cloak of Shadows",
        bonuses=[{"type": "stealth", "value": 5}]
    )
    db.session.add(cape)

    # 13. Necklace
    necklace = Necklace(
        name="Amulet of Wisdom",
        static_attributes=["Enchanted"],
        bonuses=[{"type": "knowledge", "value": 3}]
    )
    db.session.add(necklace)

    # 14. Ring
    ring = Ring(
        name="Band of Fortitude",
        static_attributes=["Gleaming"],
        bonuses=[{"type": "vigor", "value": 2}]
    )
    db.session.add(ring)

    # 15. Bonus
    bonus = Bonus(
        name="Critical Strike",
        max_roll=20,
        is_unique=True
    )
    db.session.add(bonus)

    # ─── Commit everything ───────────────────────────────────────────────────
    db.session.commit()
