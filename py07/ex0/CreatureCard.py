from .Card import Card


class CreatureCard (Card):
    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int
            ):
        super().__init__(name, cost, rarity)
        self.name = str(name)
        self.cost = int(cost)
        self.rarity = str(rarity)
        self.__health = 0
        self.__attack = 0
        self.put_attack(attack)
        self.put_health(health)
        self.type: str = 'Creature'

    def put_health(self, health):
        if int(health) >= 0:
            self.__health = int(health)
        else:
            raise ValueError("Health value must be positif")

    def put_attack(self, attack):
        if int(attack) >= 0:
            self.__attack = int(attack)
        else:
            raise ValueError("Attack value must be positif")

    def play(self, game_state: dict) -> dict:
        play_result: dict = {}
        play_result['card_played'] = self.name
        play_result['mana_used'] = self.cost
        play_result['effect'] = 'Creature summoned to battlefield'
        if game_state['mana'] < self.cost:
            return {'error': 'Not enough mana'}

        game_state['mana'] -= self.cost
        return play_result

    def get_card_info(self) -> dict:
        card_info: dict = {}
        card_info['name'] = self.name
        card_info['cost'] = self.cost
        card_info['rarity'] = self.rarity
        card_info['type'] = self.type
        card_info['attack'] = self.__attack
        card_info['health'] = self.__health
        return card_info

    def attack_target(self, target) -> dict:
        print(f"{self.name}  attacks {target}:")
        Attack_result: dict = {}
        Attack_result['attacker'] = self.name
        Attack_result['target'] = target
        Attack_result['damage_dealt'] = self.__attack
        Attack_result['combat_resolved'] = True
        return Attack_result
