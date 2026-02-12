from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from .Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")

    print("Building deck with different card types...")
    card1 = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    card2 = ArtifactCard('Mana Crystal', 2, 'Common', 5, "Permanent: +1 mana per turn")
    card3 = SpellCard("Lightning Bolt", 3, "Common", "damage")

    deck = Deck()

    deck.add_card(card1)
    deck.add_card(card2)
    deck.add_card(card3)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("Drawing and playing cards:\n")

    cards = [card1, card2, card3]

    game_state = {'mana': 17}
    ran = len(cards)
    for i in range(ran):
        deck.shuffle()
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        print(f"Play result: {card.play(game_state)}\n")
        deck.remove_card(card.name)

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
