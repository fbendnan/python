from .TournamentCard import TournamentCard

class TournamentPlatform:
    def __init__(self):
        self.cards = []
        self.cards_id = []
    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        id = card.name.split()[1]
        id = f"{id.lower()}_00{1}"
        card.id = id
        return id

    def create_match(self, card1_id: str, card2_id: str) -> dict: ...
    def get_leaderboard(self) -> list: ...
    def generate_tournament_report(self) -> dict: ...