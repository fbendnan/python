from ex0.Card import Card

class  ArtifactCard (Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = str(durability)
        self.effect = str(effect)
        self.type = 'Artifact'
    
    def play(self, game_state: dict) -> dict:
        play_result: dict = {}
        play_result['card_played'] = self.name
        play_result['mana_used'] = self.cost
        play_result['effect'] = self.effect
        return play_result
    
    def activate_ability(self) -> dict:
        ...
