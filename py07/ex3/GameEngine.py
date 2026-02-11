from .FantasyCardFactory import FantasyCardFactory
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        factory = FantasyCardFactory()
        type1 = factory.create_creature('dragon')
        type2 = factory.create_artifact('mana_ring')
        type3 = factory.create_spell('fireball')
        type4 = factory.create_creature('goblin')
        print(f"Factory : {factory.factory}")
        print(f"Strategy : {strategy.get_strategy_name()}")
        print(f'Available types: {factory.types}')

    def simulate_turn(self) -> dict: ...
    def get_engine_status(self) -> dict: ...