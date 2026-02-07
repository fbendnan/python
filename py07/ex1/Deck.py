from ex0.Card import Card

class Deck ():
    def __init__(self):
        self.cards = []
    def add_card(self, card: Card) -> None: 
        self.cards.append(card)
    
    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name.lower() == card_name.lower():
                self.cards.remove(card)

    def shuffle(self) -> None: ...
    
    def draw_card(self) -> Card: ...
    
    def get_deck_stats(self) -> dict: ...