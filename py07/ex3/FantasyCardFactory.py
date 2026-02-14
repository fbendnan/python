import random
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.types = {'creatures': [], 'spells': [], 'artifacts': []}

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        rarity = ['Legendary', 'Common', 'Rare', 'Uncommon']
        names = [
            "Fire Dragon", "Goblin Warrior",
            "Ice Wizard", "Lightning Elemental",
            "Stone Golem", "Shadow Assassin",
            "Healing Angel", "Forest Sprite"
        ]
        if isinstance(name_or_power, int):
            name = random.choice(names)
            attack = name_or_power
        elif isinstance(name_or_power, str):
            name = name_or_power
            attack = random.randint(1, 6)
        else:
            name = random.choice(names)
            attack = random.randint(1, 6)

        self.types['creatures'] += [name]
        return CreatureCard(
            name=name,
            cost=random.randint(1, 6),
            rarity=random.choice(rarity),
            attack=attack,
            health=random.randint(1, 10)
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        rarity = ['Legendary', 'Common', 'Rare', 'Uncommon']
        effects = ['damage', 'heal']
        names = [
            "Lightning Bolt", "Healing Potion",
            "Fireball", "Shield Spell",
            "Meteor", "Ice Shard",
            "Divine Light", "Magic Missile"
        ]
        if isinstance(name_or_power, int):
            name = random.choice(names)
            cost = name_or_power
        elif isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(1, 6)
        else:
            name = random.choice(names)
            cost = random.randint(1, 6)

        self.types['spells'].append(name)
        return SpellCard(
            name=name,
            cost=cost,
            rarity=random.choice(rarity),
            effect_type=random.choice(effects)
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        rarity = ['Legendary', 'Common', 'Rare', 'Uncommon']
        effects = [
            'Permanent: +1 mana per turn',
            'Permanent: +2 attack',
            'Permanent: Draw extra card'
        ]
        names = [
            "Mana Crystal", "Sword of Power",
            "Ring of Wisdom", "Shield of Defense",
            "Crown of Kings", "Boots of Speed",
            "Cloak of Shadows", "Staff of Elements"
        ]

        if isinstance(name_or_power, int):
            name = random.choice(names)
            durability = name_or_power

        elif isinstance(name_or_power, str):
            name = name_or_power
            durability = random.randint(1, 6)

        else:
            name = random.choice(names)
            durability = random.randint(1, 6)

        self.types['artifacts'].append(name)
        return ArtifactCard(
            name=name,
            cost=random.randint(1, 6),
            rarity=random.choice(rarity),
            durability=durability,
            effect=random.choice(effects)
        )

    def get_factory_card_name(self):
        return "FantasyCardFactory"

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            card_type = random.choice(['creature', 'spell', 'artifact'])
            if card_type == 'creature':
                deck.append(self.create_creature())
            elif card_type == 'spell':
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {"Hand": deck}

    def get_supported_types(self) -> dict:
        return self.types
