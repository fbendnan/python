from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy

print("=== DataDeck Game Engine ===")

print("\nConfiguring Fantasy Card Game...")
game = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()
print(game.configure_engine(factory, strategy))

print("\nSimulating aggressive turn...")

print(factory.create_themed_deck(3))