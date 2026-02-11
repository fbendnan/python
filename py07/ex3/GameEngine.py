from .FantasyCardFactory import FantasyCardFactory
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        print("Configuring Fantasy Card Game...")
        print(f"Factory: {type(factory).__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")


    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise ValueError("Engine not configured")

        deck = self.factory.create_themed_deck(3)
        hand = deck["Hand"]

        battlefield = ["Enemy Player"]

        print("\nSimulating aggressive turn...")
        hand_list_names = []
        for h in hand:
            var = f"{h.name} ({h.cost})"
            hand_list_names.append(var)
        print(f"Hand: {", ".join(hand_list_names)}")

        result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)

        print("\nTurn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {result}")

        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": 3
        }
