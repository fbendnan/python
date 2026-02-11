from .GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_available = 6
        mana_used = 0
        damage_dealt = 0
        cards_played = []
        targets_attacked = []

        sorted_hand = sorted(hand, key=lambda card: card.cost)

        for card in sorted_hand:
            if card.cost <= (mana_available - mana_used):
                mana_used += card.cost
                cards_played.append(card.name)

                if hasattr(card, "attack"):
                    damage_dealt += card.attack

                elif hasattr(card, "effect_type"):
                    if card.effect_type == "damage":
                        damage_dealt += 3

        if damage_dealt > 0:
            targets_attacked.append("Enemy Player")

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            return ["Enemy Player"] + [
                t for t in available_targets if t != "Enemy Player"
            ]
        return available_targets
