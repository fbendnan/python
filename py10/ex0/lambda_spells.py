def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_mage_power = max(mages, key=lambda mage: mage['power'])
    min_mage_power = min(mages, key=lambda mage: mage['power'])
    avg_power = sum(map(lambda mage: int(mage['power']), mages))/len(mages)

    return {
        'max_power': max_mage_power['power'],
        'min_power': min_mage_power['power'],
        'avg_power': avg_power
    }


def main():
    artifacts = [
        {'name': 'Amulet of Fire', 'power': 50, 'type': 'amulet'},
        {'name': 'Sword of Light', 'power': 80, 'type': 'sword'},
        {'name': 'Cloak of Shadows', 'power': 30, 'type': 'cloak'}
    ]
    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(sorted_artifacts)

    print("\nTesting filter power...")
    filter_power = power_filter(artifacts, 40)
    print(filter_power)

    print("\nTesting spell transformer...")
    spells = ['Fireball', 'Ice Shard', 'Lightning Bolt']
    transformed_spells = spell_transformer(spells)
    print(' '.join(transformed_spells))

    print("\nTesting mage stats...")
    print(mage_stats(artifacts))


main()
