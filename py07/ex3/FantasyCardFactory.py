import random
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.types = {
            'creatures': ['Fire Dragon', 'Goblin Warrior'],
            'spells': ['Lightning Bolt'],
            'artifacts': ['Mana Ring']
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        rarity = ['Legendary', 'Common', 'Rare', 'Uncommon']
        name = name_or_power or random.choice(self.types['creatures'])
        return CreatureCard(
            name,
            cost=random.randint(1, 6),
            rarity=random.choice(rarity),
            attack=random.randint(1, 7),
            health=random.randint(1, 10)
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        rarity = ['Legendary', 'Common', 'Rare', 'Uncommon']
        effects = ['damage', 'heal', 'buff']
        name = name_or_power or random.choice(self.types['spells'])
        return SpellCard(
            name,
            cost=random.randint(1, 6),
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
        name = name_or_power or random.choice(self.types['artifacts'])
        return ArtifactCard(
            name,
            cost=random.randint(1, 6),
            rarity=random.choice(rarity),
            durability=random.randint(2, 8),
            effect=random.choice(effects)
        )

    def create_themed_deck(self, size: int) -> dict:
        hand = []
        for _ in range(size):
            card_type = random.choice(['creature', 'spell', 'artifact'])
            if card_type == 'creature':
                hand.append(self.create_creature())
            elif card_type == 'spell':
                hand.append(self.create_spell())
            else:
                hand.append(self.create_artifact())

        return {"Hand": hand}

    def get_supported_types(self) -> dict:
        return self.types
