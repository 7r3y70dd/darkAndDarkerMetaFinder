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
    Defense_Expert = Perk(
        name="Defense Expert",
        class_name="Warrior",
        bonuses=[{"type": "vigor", "value": 2, "is_multi": False}]  # list of python dicts.  ADD IS_MULTIPLIER
    )
    db.session.add(Defense_Expert)

    Steadfast = Perk(
        name="Steadfast",
        class_name="Warrior",
        bonuses=[{"type": "vigor", "value": 2}]
    )
    db.session.add(Steadfast)

    # ─── Fighter Perks ─────────────────────────────────────────────────────────────────

    # 1. Adrenaline Spike
    Adrenaline_Spike = Perk(
        name="Adrenaline Spike",
        class_name="Fighter",
        bonuses=[{"type": "action_speed", "value": 0.15, "is_multi": True}]
    )  # :contentReference[oaicite:0]{index=0}

    db.session.add(Adrenaline_Spike)

    # 2. Barricade
    Barricade = Perk(
        name="Barricade",
        class_name="Fighter",
        bonuses=[
            {"type": "armor_rating", "value": 50, "is_multi": False},
            {"type": "magical_resistance", "value": 50, "is_multi": False}
        ]
    )  # :contentReference[oaicite:1]{index=1}

    db.session.add(Barricade)

    # 3. Combo Attack
    Combo_Attack = Perk(
        name="Combo Attack",
        class_name="Fighter",
        bonuses=[{"type": "physical_power", "value": 0.10, "is_multi": True}]
    )  # :contentReference[oaicite:2]{index=2}

    db.session.add(Barricade)

    # 4. Counterattack
    Counterattack = Perk(
        name="Counterattack",
        class_name="Fighter",
        bonuses=[
            {"type": "move_speed", "value": 0.10, "is_multi": True},
            {"type": "action_speed", "value": 0.10, "is_multi": True}
        ]
    )  # :contentReference[oaicite:3]{index=3}

    db.session.add(Barricade)


    # 5. Defense Mastery
    Defense_Mastery = Perk(
        name="Defense Mastery",
        class_name="Fighter",
        bonuses=[
            {"type": "item_armor_rating_bonus", "value": 0.10, "is_multi": True},
            {"type": "physical_damage_reduction_cap", "value": 75, "is_multi": False}
        ]
    )  # :contentReference[oaicite:4]{index=4}

    db.session.add(Barricade)


    # 6. Dual Wield
    Dual_Wield = Perk(
        name="Dual Wield",
        class_name="Fighter",
        bonuses=[{"type": "action_speed", "value": 0.10, "is_multi": True}]
    )  # :contentReference[oaicite:5]{index=5}

    db.session.add(Barricade)


    # 7. Projectile Resistance
    Projectile_Resistance = Perk(
        name="Projectile Resistance",
        class_name="Fighter",
        bonuses=[{"type": "projectile_damage_reduction", "value": 0.10, "is_multi": True}]
    )  # :contentReference[oaicite:6]{index=6}

    db.session.add(Barricade)


    # 8. Shield Mastery
    Shield_Mastery = Perk(
        name="Shield Mastery",
        class_name="Fighter",
        bonuses=[
            {"type": "move_speed", "value": 0.10, "is_multi": True},
            {"type": "action_speed", "value": 0.50, "is_multi": True}
        ]
    )  # :contentReference[oaicite:7]{index=7}

    db.session.add(Barricade)


    # 9. Slayer
    Slayer = Perk(
        name="Slayer",
        class_name="Fighter",
        bonuses=[{"type": "physical_weapon_damage", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:8]{index=8}

    db.session.add(Barricade)


    # 10. Swift
    Swift = Perk(
        name="Swift",
        class_name="Fighter",
        bonuses=[{"type": "armor_speed_penalty_reduction", "value": 0.30, "is_multi": True}]
    )  # :contentReference[oaicite:9]{index=9}

    db.session.add(Barricade)


    # 11. Sword Mastery
    Sword_Mastery = Perk(
        name="Sword Mastery",
        class_name="Fighter",
        bonuses=[
            {"type": "physical_weapon_damage", "value": 2, "is_multi": False},
            {"type": "action_speed", "value": 0.05, "is_multi": True},
            {"type": "move_speed", "value": 10, "is_multi": False}
        ]
    )  # :contentReference[oaicite:10]{index=10}

    db.session.add(Barricade)


    # 12. Weapon Mastery
    Weapon_Mastery = Perk(
        name="Weapon Mastery",
        class_name="Fighter",
        bonuses=[
            {"type": "physical_power_penalty", "value": 0.10, "is_multi": True},
            {"type": "magical_power_penalty", "value": 0.10, "is_multi": True}
        ]
    )  # :contentReference[oaicite:11]{index=11}

    db.session.add(Barricade)


    # ─── Barbarian Perks ────────────────────────────────────────────────────────────────

    # 13. Axe Specialization
    Axe_Specialization = Perk(
        name="Axe Specialization",
        class_name="Barbarian",
        bonuses=[{"type": "physical_weapon_damage", "value": 3, "is_multi": False}]
    )  # :contentReference[oaicite:12]{index=12}

    db.session.add(Barricade)


    # 14. Berserker
    Berserker = Perk(
        name="Berserker",
        class_name="Barbarian",
        bonuses=[
            # Maximum value at lowest health: 33.3% Physical Power, 33.3% Move Speed
            {"type": "physical_power", "value": 0.333, "is_multi": True},
            {"type": "move_speed", "value": 0.333, "is_multi": True}
        ]
    )  # :contentReference[oaicite:13]{index=13}

    db.session.add(Barricade)


    # 15. Carnage
    Carnage = Perk(
        name="Carnage",
        class_name="Barbarian",
        bonuses=[{"type": "armor_rating", "value": 75, "is_multi": False}]
    )  # :contentReference[oaicite:14]{index=14}

    db.session.add(Barricade)


    # 16. Executioner
    Executioner = Perk(
        name="Executioner",
        class_name="Barbarian",
        bonuses=[{"type": "physical_headshot_bonus", "value": 0.10, "is_multi": True}]
    )  # :contentReference[oaicite:15]{index=15}

    db.session.add(Barricade)


    # 17. Iron Will
    Iron_Will = Perk(
        name="Iron Will",
        class_name="Barbarian",
        bonuses=[
            {"type": "magical_resistance", "value": 75, "is_multi": False},
            {"type": "magical_damage_reduction_cap", "value": 75, "is_multi": False}
        ]
    )  # :contentReference[oaicite:16]{index=16}

    db.session.add(Barricade)


    # 18. Morale Boost
    Morale_Boost = Perk(
        name="Morale Boost",
        class_name="Barbarian",
        bonuses=[{"type": "percent_max_health_healing", "value": 0.33, "is_multi": True}]
    )  # :contentReference[oaicite:17]{index=17}

    db.session.add(Barricade)


    # 19. Potion Chugger
    Potion_Chugger = Perk(
        name="Potion Chugger",
        class_name="Barbarian",
        bonuses=[
            {"type": "healing_potency_multiplier", "value": 1.2, "is_multi": True},
            {"type": "shielding_potency_multiplier", "value": 1.2, "is_multi": True}
        ]

    )  # :contentReference[oaicite:18]{index=18}

    db.session.add(Barricade)


    # 20. Savage
    Savage = Perk(
        name="Savage",
        class_name="Barbarian",
        bonuses=[
            {"type": "physical_power", "value": 0.10, "is_multi": True},
            {"type": "impact_resistance", "value": 1, "is_multi": False}
        ]
    )  # :contentReference[oaicite:19]{index=19}

    db.session.add(Barricade)


    # 21. Crush
    Crush = Perk(
        name="Crush",
        class_name="Barbarian",
        bonuses=[{"type": "impact_power", "value": 1, "is_multi": False}]
    )  # :contentReference[oaicite:20]{index=20}

    db.session.add(Barricade)


    # 22. Robust
    Robust = Perk(
        name="Robust",
        class_name="Barbarian",
        bonuses=[{"type": "max_health", "value": 0.10, "is_multi": True}]
    )  # :contentReference[oaicite:21]{index=21}

    db.session.add(Barricade)


    # 23. Two-Hander
    Two_Hander = Perk(
        name="Two-Hander",
        class_name="Barbarian",
        bonuses=[
            {"type": "physical_power", "value": 0.05, "is_multi": True},
            {"type": "armor_penetration", "value": 0.05, "is_multi": True}
        ]
    )  # :contentReference[oaicite:22]{index=22}

    db.session.add(Barricade)


    # ─── Rogue Perks ────────────────────────────────────────────────────────────────────

    # 24. Ambush
    Ambush = Perk(
        name="Ambush",
        class_name="Rogue",
        bonuses=[{"type": "weapon_damage", "value": 0.50, "is_multi": True}]
    )  # :contentReference[oaicite:23]{index=23}

    db.session.add(Barricade)


    # 25. Backstab
    Backstab = Perk(
        name="Backstab",
        class_name="Rogue",
        bonuses=[{"type": "physical_damage_bonus", "value": 0.30, "is_multi": True}]
    )  # :contentReference[oaicite:24]{index=24}

    db.session.add(Barricade)


    # 26. Creep
    Creep = Perk(
        name="Creep",
        class_name="Rogue",
        bonuses=[{"type": "move_speed", "value": 0.05, "is_multi": True}]
    )  # :contentReference[oaicite:25]{index=25}

    db.session.add(Barricade)


    # 27. Dagger Expert
    Dagger_Expert = Perk(
        name="Dagger Expert",
        class_name="Rogue",
        bonuses=[{"type": "physical_damage_bonus", "value": 0.05, "is_multi": True}]
    )  # :contentReference[oaicite:26]{index=26}

    db.session.add(Barricade)


    # ─── Ranger Perks ───────────────────────────────────────────────────────────────────

    # 28. Ranged Weapons Mastery
    Ranged_Weapons_Mastery = Perk(
        name="Ranged Weapons Mastery",
        class_name="Ranger",
        bonuses=[{"type": "physical_power", "value": 0.05, "is_multi": True}]
    )  # :contentReference[oaicite:27]{index=27}

    db.session.add(Barricade)


    # 29. Nimble Hands
    Nimble_Hands = Perk(
        name="Nimble Hands",
        class_name="Ranger",
        bonuses=[{"type": "draw_speed", "value": 0.15, "is_multi": True}]
    )  # :contentReference[oaicite:28]{index=28}

    db.session.add(Barricade)


    # 30. Sharpshooter
    Sharpshooter = Perk(
        name="Sharpshooter",
        class_name="Ranger",
        bonuses=[{"type": "physical_headshot_bonus", "value": 0.15, "is_multi": True}]
    )  # :contentReference[oaicite:29]{index=29}

    db.session.add(Barricade)


    # 31. Kinesthesia
    Kinesthesia = Perk(
        name="Kinesthesia",
        class_name="Ranger",
        bonuses=[{"type": "move_speed", "value": 0.10, "is_multi": True}]
    )  # :contentReference[oaicite:30]{index=30}

    db.session.add(Barricade)


    # 32. Spear Proficiency
    Spear_Proficiency = Perk(
        name="Spear Proficiency",
        class_name="Ranger",
        bonuses=[{"type": "strength", "value": 10, "is_multi": False}]
    )  # :contentReference[oaicite:31]{index=31}

    db.session.add(Barricade)


    # ─── Wizard Perks ───────────────────────────────────────────────────────────────────

    # 33. Arcane Mastery
    Arcane_Mastery = Perk(
        name="Arcane Mastery",
        class_name="Wizard",
        bonuses=[{"type": "arcane_power", "value": 0.05, "is_multi": True}]
    )  # :contentReference[oaicite:32]{index=32}

    db.session.add(Barricade)


    # 34. Arcane Feedback
    Arcane_Feedback = Perk(
        name="Arcane Feedback",
        class_name="Wizard",
        bonuses=[
            {"type": "arcane_power", "value": 0.03, "is_multi": True},
            {"type": "spell_casting_speed", "value": 0.03, "is_multi": True}
        ]
    )  # :contentReference[oaicite:33]{index=33}

    db.session.add(Barricade)


    # 35. Fire Mastery
    Fire_Mastery = Perk(
        name="Fire Mastery",
        class_name="Wizard",
        bonuses=[{"type": "fire_power", "value": 0.05, "is_multi": True}]
    )
    # :contentReference[oaicite:34]{index=34}

    db.session.add(Barricade)


    # 36. Ice Shield
    Ice_Shield = Perk(
        name="Ice Shield",
        class_name="Wizard",
        bonuses=[{"type": "armor_rating", "value": 20, "is_multi": False}]
    )
    # :contentReference[oaicite:35]{index=35}

    db.session.add(Barricade)


    # 37. Mana Surge
    Mana_Surge = Perk(
        name="Mana Surge",
        class_name="Wizard",
        bonuses=[{"type": "magical_power", "value": 0.10, "is_multi": True}]
    )
    # :contentReference[oaicite:36]{index=36}

    db.session.add(Barricade)


    # 38. Melt
    Melt = Perk(
        name="Melt",
        class_name="Wizard",
        bonuses=[{"type": "target_physical_damage_reduction", "value": 0.20, "is_multi": True}]
    )
    # :contentReference[oaicite:37]{index=37}

    db.session.add(Barricade)


    # 39. Quick Chant
    Quick_Chant = Perk(
        name="Quick Chant",
        class_name="Wizard",
        bonuses=[{"type": "spell_casting_speed", "value": 0.15, "is_multi": True}]
    )
    # :contentReference[oaicite:38]{index=38}

    db.session.add(Barricade)


    # ─── Cleric Perks ──────────────────────────────────────────────────────────────────

    # 40. Advanced Healer
    Advanced_Healer = Perk(
        name="Advanced Healer",
        class_name="Cleric",
        bonuses=[{"type": "magical_healing", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:39]{index=39}

    db.session.add(Barricade)


    # 41. Blunt Weapon Mastery
    Blunt_Weapon_Mastery = Perk(
        name="Blunt Weapon Mastery",
        class_name="Cleric",
        bonuses=[{"type": "physical_power", "value": 0.15, "is_multi": True}]
    )  # :contentReference[oaicite:40]{index=40}

    db.session.add(Barricade)


    # 42. Brewmaster
    Brewmaster = Perk(
        name="Brewmaster",
        class_name="Cleric",
        bonuses=[{"type": "strength", "value": 10, "is_multi": False}]
    )  # :contentReference[oaicite:41]{index=41}

    db.session.add(Barricade)


    # 43. Faithfulness
    Faithfulness = Perk(
        name="Faithfulness",
        class_name="Cleric",
        bonuses=[
            {"type": "divine_magical_power", "value": 0.15, "is_multi": True},
            {"type": "move_speed_reduction_on_hit", "value": 0.15, "is_multi": True}
        ]
    )  # :contentReference[oaicite:42]{index=42}

    db.session.add(Barricade)


    # 44. Holy Aura
    Holy_Aura = Perk(
        name="Holy Aura",
        class_name="Cleric",
        bonuses=[
            {"type": "armor_rating", "value": 15, "is_multi": False},
            {"type": "magic_resistance", "value": 15, "is_multi": False}
        ]
    )  # :contentReference[oaicite:43]{index=43}

    db.session.add(Barricade)


    # 45. Kindness
    Kindness = Perk(
        name="Kindness",
        class_name="Cleric",
        bonuses=[{"type": "self_healing_bonus", "value": 0.15, "is_multi": True}]
    )  # :contentReference[oaicite:44]{index=44}

    db.session.add(Barricade)


    # 46. Perseverance
    Perseverance = Perk(
        name="Perseverance",
        class_name="Cleric",
        bonuses=[{"type": "damage_reduction", "value": 3, "is_multi": False}]
    )  # :contentReference[oaicite:45]{index=45}

    db.session.add(Barricade)


    # 47. Protection from Evil
    Protection_from_Evil = Perk(
        name="Protection from Evil",
        class_name="Cleric",
        bonuses=[{"type": "harmful_duration_reduction", "value": 0.50, "is_multi": True}]
    )  # :contentReference[oaicite:46]{index=46}

    db.session.add(Barricade)


    # 48. Requiem
    Requiem = Perk(
        name="Requiem",
        class_name="Cleric",
        bonuses=[{"type": "resurrected_ally_bonus", "value": 0.25, "is_multi": True}]
    )  # :contentReference[oaicite:47]{index=47}

    db.session.add(Barricade)


    # 49. Undead Slaying
    Undead_Slaying = Perk(
        name="Undead Slaying",
        class_name="Cleric",
        bonuses=[{"type": "undead_damage", "value": 0.20, "is_multi": True}]
    )  # :contentReference[oaicite:48]{index=48}

    db.session.add(Barricade)


    # ─── Bard Perks ────────────────────────────────────────────────────────────────────

    # 50. Rousing Rhythms
    Rousing_Rhythms = Perk(
        name="Rousing Rhythms",
        class_name="Bard",
        bonuses=[{"type": "all_attributes", "value": 2, "is_multi": False}]
    )  # :contentReference[oaicite:49]{index=49}

    db.session.add(Barricade)


    # 51. War Song
    War_Song = Perk(
        name="War Song",
        class_name="Bard",
        bonuses=[{"type": "physical_weapon_damage", "value": 3, "is_multi": False}]
    )  # :contentReference[oaicite:50]{index=50}

    db.session.add(Barricade)


    # 52. Rapier Mastery
    Rapier_Mastery = Perk(
        name="Rapier Mastery",
        class_name="Bard",
        bonuses=[
            {"type": "physical_weapon_damage", "value": 2, "is_multi": False},
            {"type": "action_speed", "value": 0.05, "is_multi": True}
        ]
    )  # :contentReference[oaicite:51]{index=51}

    db.session.add(Barricade)


    # 53. Wanderer's Luck
    Wanderers_Luck = Perk(
        name="Wanderer's Luck",
        class_name="Bard",
        bonuses=[{"type": "luck", "value": 50, "is_multi": False}]
    )  # :contentReference[oaicite:52]{index=52}

    db.session.add(Barricade)


    # 54. Harmonic Shield
    Harmonic_Shield = Perk(
        name="Harmonic Shield",
        class_name="Bard",
        bonuses=[{"type": "action_speed", "value": 0.50, "is_multi": True}]
    )  # :contentReference[oaicite:53]{index=53}

    db.session.add(Barricade)


    # ─── Warlock Perks ─────────────────────────────────────────────────────────────────

    # 55. Demon Armor
    Demon_Armor = Perk(
        name="Demon Armor",
        class_name="Warlock",
        bonuses=[{"type": "spell_casting_speed", "value": -0.10, "is_multi": True}]
    )  # :contentReference[oaicite:54]{index=54}

    db.session.add(Barricade)


    # 56. Immortal Lament
    Immortal_Lament = Perk(
        name="Immortal Lament",
        class_name="Warlock",
        bonuses=[]
    )  # (no direct numeric bonus) :contentReference[oaicite:55]{index=55}

    db.session.add(Barricade)


    # 57. Vampirism
    Vampirism = Perk(
        name="Vampirism",
        class_name="Warlock",
        bonuses=[{"type": "magical_healing_bonus", "value": 0.20, "is_multi": True}]
    )  # :contentReference[oaicite:56]{index=56}

    db.session.add(Barricade)


    # 58. Infernal Pledge
    Infernal_Pledge = Perk(
        name="Infernal Pledge",
        class_name="Warlock",
        bonuses=[
            {"type": "undead_damage_reduction", "value": 0.25, "is_multi": True},
            {"type": "demon_damage_reduction", "value": 0.25, "is_multi": True}
        ]
    )  # :contentReference[oaicite:57]{index=57}

    db.session.add(Barricade)


    # 59. Curse Mastery
    Curse_Mastery = Perk(
        name="Curse Mastery",
        class_name="Warlock",
        bonuses=[]
    )  # (no direct numeric bonus) :contentReference[oaicite:58]{index=58}

    db.session.add(Barricade)


    # 60. Dark Reflection
    Dark_Reflection = Perk(
        name="Dark Reflection",
        class_name="Warlock",
        bonuses=[]
    )  # (no direct numeric bonus) :contentReference[oaicite:59]{index=59}

    db.session.add(Barricade)


    # ─── Druid Perks ────────────────────────────────────────────────────────────────────

    # 61. Dreamwalk
    Dreamwalk = Perk(
        name="Dreamwalk",
        class_name="Druid",
        bonuses=[{"type": "magical_power", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:60]{index=60}

    db.session.add(Barricade)


    # 62. Force of Nature
    Force_of_Nature = Perk(
        name="Force of Nature",
        class_name="Druid",
        bonuses=[{"type": "physical_power", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:61]{index=61}

    db.session.add(Barricade)


    # 63. Wild Fury
    Wild_Fury = Perk(
        name="Wild Fury",
        class_name="Druid",
        bonuses=[
            {"type": "physical_power", "value": 5, "is_multi": False},
            {"type": "physical_damage_reduction", "value": 0.15, "is_multi": True}
        ]
    )  # :contentReference[oaicite:62]{index=62}

    db.session.add(Barricade)


    # 64. Enhanced Wildness
    Enhanced_Wildness = Perk(
        name="Enhanced Wildness",
        class_name="Druid",
        bonuses=[
            {"type": "armor_rating", "value": 10, "is_multi": False},
            {"type": "move_speed_add", "value": 5, "is_multi": False}
        ]
    )  # :contentReference[oaicite:63]{index=63}

    db.session.add(Barricade)


    # ─── Sorcerer Perks ─────────────────────────────────────────────────────────────────

    # 65. Apex of Sorcery
    Apex_of_Sorcery = Perk(
        name="Apex of Sorcery",
        class_name="Sorcerer",
        bonuses=[
            {"type": "magical_power", "value": 0.50, "is_multi": True},
            {"type": "spell_casting_speed", "value": 0.50, "is_multi": True},
            {"type": "move_speed_multiplier", "value": 0.01, "is_multi": True}
        ]
    )  # :contentReference[oaicite:64]{index=64}

    db.session.add(Barricade)


    # 66. Mana Fold
    Mana_Fold = Perk(
        name="Mana Fold",
        class_name="Sorcerer",
        bonuses=[
            {"type": "cooldown_multiplier", "value": 0.75, "is_multi": True},
            {"type": "spell_casting_speed", "value": -0.15, "is_multi": True}
        ]
    )  # :contentReference[oaicite:65]{index=65}

    db.session.add(Barricade)


    # 67. Spell Sculpting
    Spell_Sculpting = Perk(
        name="Spell Sculpting",
        class_name="Sorcerer",
        bonuses=[
            {"type": "spell_range_multiplier", "value": 1.25, "is_multi": True},
            {"type": "spell_aoe_multiplier", "value": 1.25, "is_multi": True},
            {"type": "cooldown_multiplier", "value": 1.25, "is_multi": True}
        ]
    )  # :contentReference[oaicite:66]{index=66}

    db.session.add(Barricade)


    # 68. Spell Stride
    Spell_Stride = Perk(
        name="Spell Stride",
        class_name="Sorcerer",
        bonuses=[{"type": "move_speed", "value": 0.05, "is_multi": True}]
    )  # :contentReference[oaicite:67]{index=67}

    db.session.add(Barricade)


    # 69. Innate Talent
    Innate_Talent = Perk(
        name="Innate Talent",
        class_name="Sorcerer",
        bonuses=[{"type": "all_attributes", "value": 1, "is_multi": False}]
    )  # :contentReference[oaicite:68]{index=68}

    db.session.add(Barricade)


    # 70. Merged Might
    Merged_Might = Perk(
        name="Merged Might",
        class_name="Sorcerer",
        bonuses=[]
    )  # (no direct numeric bonus) :contentReference[oaicite:69]{index=69}

    db.session.add(Barricade)


    # 71. Elemental Fury
    Elemental_Fury = Perk(
        name="Elemental Fury",
        class_name="Sorcerer",
        bonuses=[{"type": "physical_power", "value": 0.15, "is_multi": True}]
    )  # :contentReference[oaicite:70]{index=70}

    db.session.add(Barricade)


    # 72. Mana Flow
    Mana_Flow = Perk(
        name="Mana Flow",
        class_name="Sorcerer",
        bonuses=[]
    )  # (no direct numeric bonus) :contentReference[oaicite:71]{index=71}

    db.session.add(Barricade)


    # 73. Lightning Mastery
    Lightning_Mastery = Perk(
        name="Lightning Mastery",
        class_name="Sorcerer",
        bonuses=[]
    )  # (no direct numeric bonus) :contentReference[oaicite:72]{index=72}

    db.session.add(Barricade)


    # 74. Air Mastery
    Air_Mastery = Perk(
        name="Air Mastery",
        class_name="Sorcerer",
        bonuses=[]
    )

    db.session.add(Barricade)



    # 3. Skill
    skill = Skill(
        name="Lockpicking",
        class_name="Rogue",
        bonuses=[{"type": "dexterity", "value": 3}]
    )
    db.session.add(skill)

    # ─── Divinely Inspired ────────────────────────────────────────────────────────────────

    # 1. Divine Protection (Cleric)
    Divine_Protection = Skill(
        name="Divine Protection",
        class_name="Cleric",
        bonuses=[{"type": "physical_damage_reduction", "value": 0.30, "is_multi": True}]
    )  # :contentReference[oaicite:0]{index=0}

    # 2. Divine Strike (Cleric)
    Divine_Strike = Skill(
        name="Divine Strike",
        class_name="Cleric",
        bonuses=[{"type": "divine_strike_damage", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:1]{index=1}

    # ─── Primal Fury ─────────────────────────────────────────────────────────────────────

    # 3. Rage (Barbarian)
    Rage = Skill(
        name="Rage",
        class_name="Barbarian",
        bonuses=[
            {"type": "strength", "value": 15, "is_multi": False},
            {"type": "vigor", "value": 15, "is_multi": False},
            {"type": "move_speed", "value": 0.12, "is_multi": True},
            {"type": "physical_damage_reduction", "value": -0.15, "is_multi": True}
        ]
    )  # :contentReference[oaicite:2]{index=2}

    # 4. Reckless Attack (Barbarian)
    Reckless_Attack = Skill(
        name="Reckless Attack",
        class_name="Barbarian",
        bonuses=[
            {"type": "armor_penetration", "value": 0.75, "is_multi": True},
            {"type": "armor_rating", "value": -85, "is_multi": False}
        ]
    )  # :contentReference[oaicite:3]{index=3}

    # 5. Savage Roar (Barbarian)
    Savage_Roar = Skill(
        name="Savage Roar",
        class_name="Barbarian",
        bonuses=[
            {"type": "physical_power", "value": -0.30, "is_multi": True},
            {"type": "move_speed", "value": -0.05, "is_multi": True}
        ]
    )  # :contentReference[oaicite:4]{index=4}

    # 6. War Cry (Barbarian)
    War_Cry = Skill(
        name="War Cry",
        class_name="Barbarian",
        bonuses=[{"type": "max_health", "value": 0.25, "is_multi": True}]
    )  # :contentReference[oaicite:5]{index=5}

    # 7. War Sacrifice (Barbarian)
    War_Sacrifice = Skill(
        name="War Sacrifice",
        class_name="Barbarian",
        bonuses=[{"type": "all_attributes", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:6]{index=6}

    # ─── Swift and Sure ──────────────────────────────────────────────────────────────────

    # 8. Perfect Block (Fighter)
    Perfect_Block = Skill(
        name="Perfect Block",
        class_name="Fighter",
        bonuses=[{"type": "impact_resistance", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:7]{index=7}

    # 9. Second Wind (Fighter)
    Second_Wind = Skill(
        name="Second Wind",
        class_name="Fighter",
        bonuses=[{"type": "percent_max_health_healing", "value": 0.40, "is_multi": True}]
    )  # :contentReference[oaicite:8]{index=8}

    # 10. Spell Reflection (Fighter)
    Spell_Reflection = Skill(
        name="Spell Reflection",
        class_name="Fighter",
        bonuses=[]  # (No direct numerical bonuses beyond reflecting, skip)
    )  # :contentReference[oaicite:9]{index=9}

    # 11. Sprint (Fighter)
    Sprint = Skill(
        name="Sprint",
        class_name="Fighter",
        bonuses=[{"type": "move_speed", "value": 15, "is_multi": False}]
    )  # :contentReference[oaicite:10]{index=10}

    # 12. Taunt (Fighter)
    Taunt = Skill(
        name="Taunt",
        class_name="Fighter",
        bonuses=[
            {"type": "physical_damage_reduction", "value": 0.12, "is_multi": True},
            {"type": "magical_damage_reduction", "value": 0.12, "is_multi": True}
        ]
    )  # :contentReference[oaicite:11]{index=11}

    # ─── Silent Shadows ─────────────────────────────────────────────────────────────────

    # 13. Hand Crossbow Mastery (Rogue)
    Hand_Crossbow_Mastery = Skill(
        name="Hand Crossbow Mastery",
        class_name="Rogue",
        bonuses=[
            {"type": "physical_weapon_damage", "value": 2, "is_multi": False},
            {"type": "move_speed", "value": 0.05, "is_multi": True},
            {"type": "action_speed", "value": 0.10, "is_multi": True},
            {"type": "spell_casting_speed", "value": 0.10, "is_multi": True}
        ]
    )  # :contentReference[oaicite:12]{index=12}

    # 14. Thrust (Rogue)
    Thrust = Skill(
        name="Thrust",
        class_name="Rogue",
        bonuses=[{"type": "armor_penetration", "value": 0.20, "is_multi": True}]
    )  # :contentReference[oaicite:13]{index=13}

    # 15. Hide (Rogue)
    Hide = Skill(
        name="Hide",
        class_name="Rogue",
        bonuses=[]  # (No direct numerical bonus; stealth utility)
    )  # :contentReference[oaicite:14]{index=14}

    # 16. Rupture (Rogue)
    Rupture = Skill(
        name="Rupture",
        class_name="Rogue",
        bonuses=[]  # (No direct numerical stat modifications in buff)
    )  # :contentReference[oaicite:15]{index=15}

    # 17. Weakpoint Attack (Rogue)
    Weakpoint_Attack = Skill(
        name="Weakpoint Attack",
        class_name="Rogue",
        bonuses=[]  # (Effect is situational; no flat stat)
    )  # :contentReference[oaicite:16]{index=16}

    # ─── Eyes of the Hunt ─────────────────────────────────────────────────────────────────

    # 18. Penetrating Shot (Ranger)
    Penetrating_Shot = Skill(
        name="Penetrating Shot",
        class_name="Ranger",
        bonuses=[
            {"type": "physical_headshot_penetration", "value": 0.50, "is_multi": True},
            {"type": "armor_penetration", "value": 0.25, "is_multi": True}
        ]
    )  # :contentReference[oaicite:17]{index=17}

    # 19. Purge Shot (Ranger)
    Purge_Shot = Skill(
        name="Purge Shot",
        class_name="Ranger",
        bonuses=[]  # (No flat or percentage stat shown)
    )  # :contentReference[oaicite:18]{index=18}

    # 20. Quick Fire (Ranger)
    Quick_Fire = Skill(
        name="Quick Fire",
        class_name="Ranger",
        bonuses=[]  # (No direct stat change, only attack effect)
    )  # :contentReference[oaicite:19]{index=19}

    # 21. Quick Reload (Ranger)
    Quick_Reload = Skill(
        name="Quick Reload",
        class_name="Ranger",
        bonuses=[{"type": "action_speed", "value": 0.50, "is_multi": True}]
    )  # :contentReference[oaicite:20]{index=20}

    # 22. Ranged Weapons Mastery (Ranger)
    Ranged_Weapons_Mastery = Skill(
        name="Ranged Weapons Mastery",
        class_name="Ranger",
        bonuses=[{"type": "physical_power", "value": 0.05, "is_multi": True}]
    )  # :contentReference[oaicite:21]{index=21}

    # 23. True Shot (Ranger)
    True_Shot = Skill(
        name="True Shot",
        class_name="Ranger",
        bonuses=[{"type": "physical_power", "value": 0.08, "is_multi": True}]
    )  # :contentReference[oaicite:22]{index=22}

    # ─── Nature’s Touch ────────────────────────────────────────────────────────────────

    # 24. Force Of Nature (Druid)
    Force_Of_Nature = Skill(
        name="Force Of Nature",
        class_name="Druid",
        bonuses=[{"type": "physical_power", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:23]{index=23}

    # 25. Frenzied (Druid)
    Frenzied = Skill(
        name="Frenzied",
        class_name="Druid",
        bonuses=[]  # (No direct stat modifications displayed)
    )  # :contentReference[oaicite:24]{index=24}

    # 26. Herbal Sensing (Druid)
    Herbal_Sensing = Skill(
        name="Herbal Sensing",
        class_name="Druid",
        bonuses=[]  # (Discovery utility, no flat stat)
    )  # :contentReference[oaicite:25]{index=25}

    # 27. Prophecy (Druid)
    Prophecy = Skill(
        name="Prophecy",
        class_name="Druid",
        bonuses=[]  # (No direct stat change)
    )  # :contentReference[oaicite:26]{index=26}

    # 28. Spirit Magic Mastery (Druid)
    Spirit_Magic_Mastery = Skill(
        name="Spirit Magic Mastery",
        class_name="Druid",
        bonuses=[{"type": "magical_power", "value": 10, "is_multi": False}]
    )  # :contentReference[oaicite:27]{index=27}

    # 29. Survival Instinct (Druid)
    Survival_Instinct = Skill(
        name="Survival Instinct",
        class_name="Druid",
        bonuses=[
            {"type": "max_health", "value": 10, "is_multi": False},
            {"type": "move_speed", "value": 20, "is_multi": False}
        ]
    )  # :contentReference[oaicite:28]{index=28}

    # 30. Thorn Coat (Druid)
    Thorn_Coat = Skill(
        name="Thorn Coat",
        class_name="Druid",
        bonuses=[]  # (No direct numerical stat change)
    )  # :contentReference[oaicite:29]{index=29}

    # 31. Tree of Life (Druid)
    Tree_Of_Life = Skill(
        name="Tree of Life",
        class_name="Druid",
        bonuses=[{"type": "recoverable_health", "value": 20, "is_multi": False}]
    )  # :contentReference[oaicite:30]{index=30}

    # ─── Arcane Precision ────────────────────────────────────────────────────────────────

    # 32. Arcane Shield (Wizard)
    Arcane_Shield = Skill(
        name="Arcane Shield",
        class_name="Wizard",
        bonuses=[{"type": "base_shield", "value": 15, "is_multi": False}]
    )  # :contentReference[oaicite:31]{index=31}

    # 33. Glaciate (Wizard)
    Glaciate = Skill(
        name="Glaciate",
        class_name="Wizard",
        bonuses=[]  # (Effect is Frostbite on enemy; no direct buff stat)
    )  # :contentReference[oaicite:32]{index=32}

    # 34. Quick Chant (Wizard)
    Quick_Chant = Skill(
        name="Quick Chant",
        class_name="Wizard",
        bonuses=[{"type": "spell_casting_speed", "value": 0.15, "is_multi": True}]
    )  # :contentReference[oaicite:33]{index=33}

    # 35. Reactive Shield (Wizard)
    Reactive_Shield = Skill(
        name="Reactive Shield",
        class_name="Wizard",
        bonuses=[{"type": "base_shield", "value": 15, "is_multi": False}]
    )  # :contentReference[oaicite:34]{index=34}

    # 36. Sage (Wizard)
    Sage = Skill(
        name="Sage",
        class_name="Wizard",
        bonuses=[{"type": "knowledge", "value": 10, "is_multi": True}]
    )  # :contentReference[oaicite:35]{index=35}

    # 37. Spell Overload (Wizard)
    Spell_Overload = Skill(
        name="Spell Overload",
        class_name="Wizard",
        bonuses=[
            {"type": "knowledge", "value": -0.20, "is_multi": True},
            {"type": "max_spell_count", "value": 0.60, "is_multi": True}
        ]
    )  # :contentReference[oaicite:36]{index=36}

    # 38. Spell Reflection (Wizard)
    Spell_Reflection_Wiz = Skill(
        name="Spell Reflection",
        class_name="Wizard",
        bonuses=[]  # (Reflects spells; no direct stat buff)
    )  # :contentReference[oaicite:37]{index=37}

    # 39. Sprint (Wizard)
    # (Wizard does not have Sprint as an active; skip)

    # ─── Harmonious Resonance ────────────────────────────────────────────────────────────

    # 40. Accelerando (Bard)
    Accelerando = Skill(
        name="Accelerando",
        class_name="Bard",
        bonuses=[
            {"type": "move_speed", "value": 0.05, "is_multi": True},
            {"type": "action_speed", "value": 0.10, "is_multi": True},
            {"type": "spell_casting_speed", "value": 0.10, "is_multi": True}
        ]
    )  # :contentReference[oaicite:38]{index=38}

    # 41. Ambush (Bard)
    Ambush_Bard = Skill(
        name="Ambush",
        class_name="Bard",
        bonuses=[{"type": "move_speed", "value": 0.10, "is_multi": True}]
    )  # :contentReference[oaicite:39]{index=39}

    # 42. Rapier Mastery (Bard)
    Rapier_Mastery = Skill(
        name="Rapier Mastery",
        class_name="Bard",
        bonuses=[
            {"type": "physical_weapon_damage", "value": 2, "is_multi": False},
            {"type": "action_speed", "value": 0.05, "is_multi": True}
        ]
    )  # :contentReference[oaicite:40]{index=40}

    # 43. War Song (Bard)
    War_Song = Skill(
        name="War Song",
        class_name="Bard",
        bonuses=[{"type": "physical_weapon_damage", "value": 3, "is_multi": False}]
    )  # :contentReference[oaicite:41]{index=41}

    # 44. Wanderer’s Luck (Bard)
    Wanderers_Luck = Skill(
        name="Wanderer’s Luck",
        class_name="Bard",
        bonuses=[{"type": "luck", "value": 50, "is_multi": False}]
    )  # :contentReference[oaicite:42]{index=42}

    # 45. Harmonic Shield (Bard)
    Harmonic_Shield = Skill(
        name="Harmonic Shield",
        class_name="Bard",
        bonuses=[{"type": "move_speed", "value": 0.05, "is_multi": True}]
    )  # :contentReference[oaicite:43]{index=43}

    # ─── Ominous Mysteries ───────────────────────────────────────────────────────────────

    # 46. Abyssal Flame (Warlock)
    Abyssal_Flame = Skill(
        name="Abyssal Flame",
        class_name="Warlock",
        bonuses=[]  # (Effect is damage over time on enemies; no direct player buff)
    )  # :contentReference[oaicite:44]{index=44}

    # 47. Demon Armor (Warlock)
    Demon_Armor = Skill(
        name="Demon Armor",
        class_name="Warlock",
        bonuses=[{"type": "spell_casting_speed", "value": -0.10, "is_multi": True}]
    )  # :contentReference[oaicite:45]{index=45}

    # 48. Exploitation Strike (Warlock)
    Exploitation_Strike = Skill(
        name="Exploitation Strike",
        class_name="Warlock",
        bonuses=[]  # (Damage amplification; no flat buff)
    )  # :contentReference[oaicite:46]{index=46}

    # 49. Phantomize (Warlock)
    Phantomize = Skill(
        name="Phantomize",
        class_name="Warlock",
        bonuses=[]  # (Teleport utility; no direct stat)
    )  # :contentReference[oaicite:47]{index=47}

    # 50. Shadow Touch (Warlock)
    Shadow_Touch = Skill(
        name="Shadow Touch",
        class_name="Warlock",
        bonuses=[]  # (Shadow damage; no player buff)
    )  # :contentReference[oaicite:48]{index=48}

    # ─── Elemental Fury ─────────────────────────────────────────────────────────────────

    # 51. Forceful Shot (Ranger)
    # (No direct numeric stat change shown; skip)

    # 52. True Shot (Ranger) – already listed above.

    # 53. Glaciate (Wizard) – already listed above.

    # 54. Quick Chant (Wizard) – already listed above.

    # 55. Frenzied (Druid) – already listed above.

    # 56. Tree of Life (Druid) – already listed above.

    # 57. Sprint (Fighter) – already listed above.

    # 58. Survival Instinct (Druid) – already listed above.

    # 59. Divine Protection (Cleric) – already listed above.

    # 60. Divine Strike (Cleric) – already listed above.

    # ─── End of Skills ─────────────────────────────────────────────────────────────────────

    db.session.add(Divine_Protection)
    db.session.add(Divine_Strike)
    db.session.add(Rage)
    db.session.add(Reckless_Attack)
    db.session.add(Savage_Roar)
    db.session.add(War_Cry)
    db.session.add(War_Sacrifice)
    db.session.add(Perfect_Block)
    db.session.add(Second_Wind)
    db.session.add(Spell_Reflection)
    db.session.add(Sprint)
    db.session.add(Taunt)
    db.session.add(Hand_Crossbow_Mastery)
    db.session.add(Thrust)
    db.session.add(Hide)
    db.session.add(Rupture)
    db.session.add(Weakpoint_Attack)
    db.session.add(Penetrating_Shot)
    db.session.add(Purge_Shot)
    db.session.add(Quick_Fire)
    db.session.add(Quick_Reload)
    db.session.add(Ranged_Weapons_Mastery)
    db.session.add(True_Shot)
    db.session.add(Force_Of_Nature)
    db.session.add(Frenzied)
    db.session.add(Herbal_Sensing)
    db.session.add(Prophecy)
    db.session.add(Spirit_Magic_Mastery)
    db.session.add(Survival_Instinct)
    db.session.add(Thorn_Coat)
    db.session.add(Tree_Of_Life)
    db.session.add(Arcane_Shield)
    db.session.add(Glaciate)
    db.session.add(Quick_Chant)
    db.session.add(Reactive_Shield)
    db.session.add(Sage)
    db.session.add(Spell_Overload)
    db.session.add(Spell_Reflection_Wiz)
    db.session.add(Accelerando)
    db.session.add(Ambush_Bard)
    db.session.add(Rapier_Mastery)
    db.session.add(War_Song)
    db.session.add(Wanderers_Luck)
    db.session.add(Harmonic_Shield)
    db.session.add(Abyssal_Flame)
    db.session.add(Demon_Armor)
    db.session.add(Exploitation_Strike)
    db.session.add(Phantomize)
    db.session.add(Shadow_Touch)

    # 4. Spell
    # ─── Bard Spells ─────────────────────────────────────────────────────────────────

    Accelerando = Spell(
        name="Accelerando",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[]
    )  # :contentReference[oaicite:0]{index=0}
    db.session.add(Accelerando)

    Allegro = Spell(
        name="Allegro",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[]
    )  # :contentReference[oaicite:1]{index=1}
    db.session.add(Allegro)

    Aria_of_Alacrity = Spell(
        name="Aria of Alacrity",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "physical_power", "value": 39, "is_multi": False}]
    )  # :contentReference[oaicite:2]{index=2}
    db.session.add(Aria_of_Alacrity)

    Ballad_of_Courage = Spell(
        name="Ballad of Courage",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "move_speed", "value": 25, "is_multi": False}]
    )  # :contentReference[oaicite:3]{index=3}
    db.session.add(Ballad_of_Courage)

    Banshees_Howl = Spell(
        name="Banshees Howl",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "all_stats_reduction", "value": 1, "is_multi": False}]
    )  # :contentReference[oaicite:4]{index=4}
    db.session.add(Banshees_Howl)

    Beats_of_Alacrity = Spell(
        name="Beats of Alacrity",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "move_speed", "value": 25, "is_multi": False}]
    )  # :contentReference[oaicite:5]{index=5}
    db.session.add(Beats_of_Alacrity)

    Chaotic_Discord = Spell(
        name="Chaotic Discord",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:6]{index=6}
    db.session.add(Chaotic_Discord)

    Chorale_of_Clarity = Spell(
        name="Chorale of Clarity",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "spell_memory_restore_per_second", "value": 8, "is_multi": False}]
    )  # :contentReference[oaicite:7]{index=7}
    db.session.add(Chorale_of_Clarity)

    Din_of_Darkness = Spell(
        name="Din of Darkness",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:8]{index=8}
    db.session.add(Din_of_Darkness)

    Harmonic_Shield_Bard = Spell(
        name="Harmonic Shield",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[
            {"type": "armor_rating", "value": 50, "is_multi": False},
            {"type": "magic_resistance", "value": 50, "is_multi": False}
        ]
    )  # :contentReference[oaicite:9]{index=9}
    db.session.add(Harmonic_Shield_Bard)

    Lament_of_Languor = Spell(
        name="Lament of Languor",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "move_speed_reduction", "value": 20, "is_multi": False}]
    )  # :contentReference[oaicite:10]{index=10}
    db.session.add(Lament_of_Languor)

    Peacemaking = Spell(
        name="Peacemaking",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:11]{index=11}
    db.session.add(Peacemaking)

    Piercing_Shrill = Spell(
        name="Piercing Shrill",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "physical_damage", "value": 15, "is_multi": False}]
    )  # :contentReference[oaicite:12]{index=12}
    db.session.add(Piercing_Shrill)

    Rousing_Rhythms_Spell = Spell(
        name="Rousing Rhythms",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "all_attributes", "value": 1, "is_multi": False}]
    )  # :contentReference[oaicite:13]{index=13}
    db.session.add(Rousing_Rhythms_Spell)

    Shriek_of_Weakness = Spell(
        name="Shriek of Weakness",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[
            {"type": "physical_power_reduction", "value": 2, "is_multi": False},
            {"type": "armor_rating_reduction", "value": 30, "is_multi": False}
        ]
    )  # :contentReference[oaicite:14]{index=14}
    db.session.add(Shriek_of_Weakness)

    Song_of_Shadow = Spell(
        name="Song of Shadow",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[]
    )  # :contentReference[oaicite:15]{index=15}
    db.session.add(Song_of_Shadow)

    Song_of_Silence = Spell(
        name="Song of Silence",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:16]{index=16}
    db.session.add(Song_of_Silence)

    Tranquility = Spell(
        name="Tranquility",
        class_name="Bard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "health_restoration_per_second", "value": 8, "is_multi": False}]
    )  # :contentReference[oaicite:17]{index=17}
    db.session.add(Tranquility)

    Unchained_Harmony = Spell(
        name="Unchained Harmony",
        class_name="Bard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:18]{index=18}
    db.session.add(Unchained_Harmony)


    # ─── Cleric Spells ─────────────────────────────────────────────────────────────────

    Bind = Spell(
        name="Bind",
        class_name="Cleric",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:19]{index=19}
    db.session.add(Bind)

    Bless = Spell(
        name="Bless",
        class_name="Cleric",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[
            {"type": "strength", "value": 3, "is_multi": False},
            {"type": "agility", "value": 3, "is_multi": False},
            {"type": "will", "value": 3, "is_multi": False}
        ]
    )  # :contentReference[oaicite:20]{index=20}
    db.session.add(Bless)

    Cleanse = Spell(
        name="Cleanse",
        class_name="Cleric",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:21]{index=21}
    db.session.add(Cleanse)

    Divine_Strike_Spell = Spell(
        name="Divine Strike",
        class_name="Cleric",
        is_modifier=True,
        is_selfcast=False,
        bonuses=[{"type": "physical_weapon_damage", "value": 10, "is_multi": False}]
    )  # :contentReference[oaicite:22]{index=22}
    db.session.add(Divine_Strike_Spell)

    Holy_Light = Spell(
        name="Holy Light",
        class_name="Cleric",
        is_modifier=False,
        is_selfcast=True,
        bonuses=[
            {"type": "healing", "value": 30, "is_multi": False},
            {"type": "magical_damage", "value": 100, "is_multi": False}
        ]
    )  # :contentReference[oaicite:23]{index=23}
    db.session.add(Holy_Light)

    Lesser_Heal = Spell(
        name="Lesser Heal",
        class_name="Cleric",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "healing", "value": 15, "is_multi": False}]
    )  # :contentReference[oaicite:24]{index=24}
    db.session.add(Lesser_Heal)

    Locusts_Swarm = Spell(
        name="Locusts Swarm",
        class_name="Cleric",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "damage_per_second", "value": 2, "is_multi": False}]
    )  # :contentReference[oaicite:25]{index=25}
    db.session.add(Locusts_Swarm)

    Protection = Spell(
        name="Protection",
        class_name="Cleric",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "shield_amount", "value": 20, "is_multi": False}]
    )  # :contentReference[oaicite:26]{index=26}
    db.session.add(Protection)

    Resurrection = Spell(
        name="Resurrection",
        class_name="Cleric",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:27]{index=27}
    db.session.add(Resurrection)

    Sanctuary = Spell(
        name="Sanctuary",
        class_name="Cleric",
        is_modifier=True,
        is_selfcast=False,
        bonuses=[
            {"type": "healing_per_second", "value": 7, "is_multi": False},
            {"type": "undead_damage_per_second", "value": 14, "is_multi": False}
        ]
    )  # :contentReference[oaicite:28]{index=28}
    db.session.add(Sanctuary)


    # ─── Wizard Spells ─────────────────────────────────────────────────────────────────

    Chain_Lightning = Spell(
        name="Chain Lightning",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:29]{index=29}
    db.session.add(Chain_Lightning)

    Fireball_Spell = Spell(
        name="Fireball",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[
            {"type": "spell_damage", "value": 30, "is_multi": False},
            {"type": "splash_damage", "value": 10, "is_multi": False}
        ]
    )  # :contentReference[oaicite:30]{index=30}
    db.session.add(Fireball_Spell)

    Haste = Spell(
        name="Haste",
        class_name="Wizard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[
            {"type": "move_speed", "value": 0.14, "is_multi": True},
            {"type": "action_speed", "value": 0.14, "is_multi": True}
        ]
    )  # :contentReference[oaicite:31]{index=31}
    db.session.add(Haste)

    Ice_Bolt = Spell(
        name="Ice Bolt",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "move_speed_reduction", "value": 0.15, "is_multi": True}]
    )  # :contentReference[oaicite:32]{index=32}
    db.session.add(Ice_Bolt)

    Ignite = Spell(
        name="Ignite",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "spell_damage", "value": 5, "is_multi": False}]
    )  # :contentReference[oaicite:33]{index=33}
    db.session.add(Ignite)

    Invisibility = Spell(
        name="Invisibility",
        class_name="Wizard",
        is_modifier=True,
        is_selfcast=True,
        bonuses=[{"type": "move_speed", "value": 0.10, "is_multi": True}]
    )  # :contentReference[oaicite:34]{index=34}
    db.session.add(Invisibility)

    Light_Orb = Spell(
        name="Light Orb",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:35]{index=35}
    db.session.add(Light_Orb)

    Lightning_Strike = Spell(
        name="Lightning Strike",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:36]{index=36}
    db.session.add(Lightning_Strike)

    Magic_Missile_Spell = Spell(
        name="Magic Missile",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "spell_damage", "value": 12, "is_multi": False}]
    )  # :contentReference[oaicite:37]{index=37}
    db.session.add(Magic_Missile_Spell)

    Slow_Spell = Spell(
        name="Slow",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "move_speed_reduction", "value": 0.40, "is_multi": True}]
    )  # :contentReference[oaicite:38]{index=38}
    db.session.add(Slow_Spell)

    Zap = Spell(
        name="Zap",
        class_name="Wizard",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[]
    )  # :contentReference[oaicite:39]{index=39}
    db.session.add(Zap)


    # ─── Warlock Spells ─────────────────────────────────────────────────────────────────

    Curse_of_Pain = Spell(
        name="Curse of Pain",
        class_name="Warlock",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "spell_damage", "value": 10, "is_multi": False}]
    )  # :contentReference[oaicite:40]{index=40}
    db.session.add(Curse_of_Pain)

    Curse_of_Weaken = Spell(
        name="Curse of Weaken",
        class_name="Warlock",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "all_stats_reduction", "value": 0.20, "is_multi": True}]
    )  # :contentReference[oaicite:41]{index=41}
    db.session.add(Curse_of_Weaken)

    Hellfire = Spell(
        name="Hellfire",
        class_name="Warlock",
        is_modifier=False,
        is_selfcast=False,
        bonuses=[{"type": "damage_per_second", "value": 60, "is_multi": False}]
    )  # :contentReference[oaicite:42]{index=42}
    db.session.add(Hellfire)

    Power_of_Sacrifice = Spell(
        name="Power of Sacrifice",
        class_name="Warlock",
        is_modifier=True,
        is_selfcast=False,
        bonuses=[
            {"type": "health_loss_per_second", "value": 3, "is_multi": False},
            {"type": "strength", "value": 15, "is_multi": False}
        ]
    )  # :contentReference[oaicite:43]{index=43}
    db.session.add(Power_of_Sacrifice)


    # 5. Weapon
    weapon = Weapon(
        name="Longsword",
        class_name=['class 1', 'class 2'],
        damage=43,
        static_attributes={"Vigor": 6, "strength": 5},
        rarity="Rare"
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
