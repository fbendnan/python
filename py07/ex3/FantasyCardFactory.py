from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
import random

class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.types = {
            'creatures' : [], 'spells' : [], 'artifacts': []
            }
        self.factory = 'FantasyCardFactory'
        self.strategy = 'AggressiveStrategy'

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        rarity = ['Legendary', 'Common', 'Rare', 'Uncommon']
        health = random.randint(1, 10)
        attack = random.randint(1, 7)
        cost = random.randint(1, 6)
        self.types['creatures'].append(str(name_or_power))

        return CreatureCard(str(name_or_power), cost, random.choices(rarity, k=4), attack, health)
    
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        rarity = ['Legendary', 'Common', 'Rare', 'Uncommon']
        effect_type = ['damage', 'heal', 'buff']
        cost = random.randint(1, 6)
        self.types['spells'].append(str(name_or_power))

        return SpellCard(str(name_or_power), cost, random.choices(rarity, k=4), random.choices(effect_type, k=3))
    
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        rarity = ['Legendary', 'Common', 'Rare', 'Uncommon']
        effect = [
            'Permanent: +1 mana per turn', 'Permanent: +2 attack to equipped creature',
            'Permanent: Draw an extra card each turn', 'Permanent: Cards cost 1 less mana',
            'Permanent: +3 health to all friendly creatures']
        cost = random.randint(1, 6)
        durability = random.randint(2, 8)
        self.types['artifacts'].append(str(name_or_power))

        return ArtifactCard(name_or_power, cost, random.choices(rarity, k=4), durability, random.choices(effect, k = 5))
    
    def create_themed_deck(self, size: int) -> dict:
        names = ['Fire Dragon', 'Goblin Warrior', 'Lightning Bolt']
        card_types = [self.create_artifact(), self.create_spell(), self.create_creature()]
        hand = {'Hand': []}
        for i in range(size):
            card = random.choices(card_types, k = 3)
            name = random.choices(names, k = 3)
            hand_s = card(name)
            hand['Hand'].append(f'{hand_s} ({hand_s.health})')


    def get_supported_types(self) -> dict:
        return self.types

