from ex0.Card import Card

class  SpellCard (Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = str(effect_type)
        self.type = 'Spell'

    def play(self, game_state: dict) -> dict:
        play_result: dict = {}
        play_result['card_played'] = self.name
        play_result['mana_used'] = self.cost
        play_result['effect'] = f'Deal {self.cost} {self.effect_type} to target'
        if game_state['mana'] < self.cost:
            return {'error': 'Not enough mana'}

        game_state['mana'] -= self.cost
        return play_result
    
    def resolve_effect(self, targets: list) -> dict:
        ...