
def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulator(amount: int):
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key, value):
        vault[key] = value

    def recall(key):
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main():
    counter = mage_counter()
    print("\nTesting mage counter...")
    for i in range(3):
        print(f"Cell {i + 1}: {counter()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(10)
    print(f"add 5: {acc(5)}")
    print(f"add 3: {acc(3)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))
    
    print("\nTesting memory vault...")
    mem = memory_vault()
    mem['store']("spell1", "Fireball")
    print(mem['recall']("spell1"))
    print(mem['recall']("spell2"))


if __name__ == "__main__":
    main()