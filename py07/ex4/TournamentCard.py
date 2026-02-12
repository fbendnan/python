from ex0.Card import Card
from .Rankable import Rankable
from ex2.Combatable import Combatable
import random

class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.interfaces = ["Card, Combatable, Rankable"]
        self.defense_result = {}
        self.attack_result = {}
        self.id = ""
        self.rating = 0
        self.win_times = 0
        self.lose_times = 0
        self.rank = 0

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

    def calculate_rating(self) -> int:
        self.rating = random.randint(900, 1500)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.win_times += wins

    def update_losses(self, losses: int) -> None:
        self.lose_times += losses

    def get_rank_info(self) -> dict:
        rank_info = {
            self.rank : f"{self.name} - Rating: {self.rating} ({self.win_times}-{self.lose_times})"
        }
        return rank_info
    
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
    def get_tournament_stats(self) -> dict: ...
