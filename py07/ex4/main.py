from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")
    tournement_card1 = TournamentCard("Fire Dragon", 5, "rare")
    plateform = TournamentPlatform()
    tournement_card2 = TournamentCard("Ice Wizard", 5, "rare")

    print("Registering Tournament Cards...")
    print(plateform.register_card(tournement_card1))
    print()
    print(plateform.register_card(tournement_card2))

    print("\nCreating tournament match...")
    print(plateform.create_match(tournement_card1.id, tournement_card2.id))

    print("\nTournament Leaderboard:")
    leaderboard = plateform.get_leaderboard()
    i: int = 1
    for player in leaderboard:
        print(f"{i}. {player[i]}")
        i += 1

    print("\nPlatform Report:")
    print(plateform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ==="
          "\nAll abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
