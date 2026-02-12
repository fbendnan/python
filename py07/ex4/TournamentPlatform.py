from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches = 0
        self.avg_rating = 0

    def register_card(self, card: TournamentCard) -> str:
        id = card.name.split()[1]
        id = f"{id.lower()}_00{1}"
        card.id = id
        self.cards[id] = card
        return (f"{card.name}({id})"
                f"\n-Interfaces {card.interfaces}"
                f"\n-Rating: {card.calculate_rating()}"
                f"\n-Record: {card.win_times}-{card.lose_times}")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches += 1
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        if card1.rating > card2.rating:
            winner_card = card1
            loser_card = card2
        elif card2.rating > card1.rating:
            winner_card = card2
            loser_card = card1
        else:
            return {
                'winner_cards': f"{card1.name} and {card2.name}",
                'rating': card2.rating
            }
        winner_card.update_wins(1)
        winner_card.rank = 1
        loser_card.update_losses(1)
        loser_card.rank = 2
        return {
            'winner': winner_card.id, 'loser': loser_card.id,
            'winner_rating': winner_card.rating,
            'loser_rating': loser_card.rating
        }

    def get_leaderboard(self) -> list:
        board_ranking = []
        for id, card in self.cards.items():
            info = card.get_rank_info()
            board_ranking.append(info)
        sorted_board = sorted(board_ranking, key=lambda d: list(d.keys())[0])
        return sorted_board

    def generate_tournament_report(self) -> dict:
        self.avg_rating = sum(
            card.rating for card in self.cards.values()
            )/len(self.cards)
        return {
            'total_cards': len(self.cards), 'matches_played': self.matches,
            'avg_rating': self.avg_rating, 'platform_status': 'active'
        }
