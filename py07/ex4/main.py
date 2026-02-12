from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform
print("=== DataDeck Tournament Platform ===\n")
tournement = TournamentCard("Fire Dragon", 5, "rare")
plateform = TournamentPlatform()

print(f"{tournement.name} ({plateform.register_card(tournement)})")
print(tournement.interfaces)
print(tournement.calculate_rating())