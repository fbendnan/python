from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ArtifactCard import ArtifactCard
from SpellCard import SpellCard
import random

class Deck ():
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None: 
        self.cards.append(card)
    
    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name.lower() == card_name.lower():
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    def draw_card(self) -> Card:
        if len(self.cards) > 0:
            return self.cards[0]
        else:
            return None

    def get_deck_stats(self) -> dict:
        deck_state = {}
        deck_state['total_cards'] = len(self.cards)
        deck_state['creatures'] = 0
        deck_state['spells'] = 0
        deck_state['artifacts'] = 0
        total_cost = 0
        for card in self.cards:
            if isinstance(card, CreatureCard):
                deck_state['creatures'] += 1
            elif isinstance(card, SpellCard):
                deck_state['spells'] += 1
            elif isinstance(card, ArtifactCard):
                deck_state['artifacts'] += 1
            total_cost += card.cost

        deck_state['avg_cost'] = total_cost / len(self.cards)

        return deck_state
