from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical
import random


class EliteCard (Card, Combatable, Magical):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.defense_result = {}
        self.attack_result = {}

    def play(self, game_state: dict) -> dict:
        play_result: dict = {}
        play_result['card_played'] = self.name
        play_result['mana_used'] = self.cost
        play_result['effect'] = 'Creature summoned to battlefield'
        if game_state['mana'] < self.cost:
            return {'error': 'Not enough mana'}
        game_state['mana'] -= self.cost
        return play_result

    def attack(self, target) -> dict:
        self.attack_result = {
            "attcker": self.name, "target": target, 'damage': 5,
            'combat_type': self.rarity
        }
        return self.attack_result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            "channeled": amount - self.cost,
            "total_mana": amount
        }

    def get_magic_stats(self) -> dict:
        return {
            'magic_state': 'magic'
        }

    def defend(self, incoming_damage: int) -> dict:
        self.defense_result = {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": random.randint(0, incoming_damage),
            "still_alive": random.choice([True, False])
        }
        return self.defense_result

    def get_combat_stats(self) -> dict:
        return {
            "combat_state": [self.attack_result, self.defense_result]
        }
