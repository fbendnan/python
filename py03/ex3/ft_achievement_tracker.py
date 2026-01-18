def main():
    print("=== Achievement Tracker System ===\n")

    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements = alice | bob | charlie
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common = alice & bob & charlie
    print(f"\nCommon to all players: {common}")

    rare = (
        alice.difference(bob | charlie)
        | bob.difference(alice | charlie)
        | charlie.difference(alice | bob)
    )
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    main()
