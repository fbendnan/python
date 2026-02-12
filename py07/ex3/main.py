from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    engine = GameEngine()

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)
    engine.simulate_turn()

    print("\nGame Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":  
    try:
        main()
    except Exception as e:
        print(e)
