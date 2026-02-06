from CreatureCard import CreatureCard
from typing import Any


def Game_start(is_playable: bool, card1: Any, game_state: dict):
    if is_playable:
        print("Playable: True")
        print(f"Play result: {card1.play(game_state)}\n")
        attack_result: dict = card1.attack_target('Goblin Warrior')
        print(f"Attack result: {attack_result}\n")
    elif is_playable is False:
        print("Playable: False")


def main():
    try:
        print("=== DataDeck Card Foundation ===\n")
        print("Testing Abstract Base Class Design:\n")

        card1 = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        print("CreatureCard Info:")
        print(card1.get_card_info())

        game_state = {
            'mana': 6, 'effect': 'Creature summoned to battlefield'
            }
        print(f"\nPlaying Fire Dragon with {game_state['mana']} "
              "mana available:")
        Game_start(card1.is_playable(game_state['mana']), card1, game_state)

        game_state_2 = {
            'mana': 3, 'effect': 'Creature summoned to battlefield'
            }
        print(f"Testing insufficient mana ({game_state_2['mana']} available):")
        Game_start(card1.is_playable(game_state_2['mana']),
                   card1, game_state_2)

    except Exception as e:
        print(f"Error: {e}")

    print("\nAbstract pattern successfully demonstrated!")


main()
