def player_inventory(players):
    print("=== Player Inventory System ===")
    inventory_value = 0
    item_count = 0
    categories = {}

    for keys, values in players["alice"].items():
        inventory_value += (values.get("value") * values.get("quantity"))
        item_count += values.get("quantity")

        item_type = values.get("type")
        categories[item_type] = categories.get(item_type, 0) + values.get("quantity")

        print(f"{keys} ({values.get('type')}, {values.get('rarity')}): "
              f"{values.get('quantity')}x @ {values.get('value')} gold "
              f"each = {values.get('value') * values.get('quantity')} gold")

    print(f"\nInventory value: {inventory_value} gold"
          f"\nItem count: {item_count} items")

    print("Categories: ", end="")
    last = False
    for k, v in categories.items():
        if last is True:
            print(", ", end="")
        print(f"{k}({v})", end="")
        last = True
    print()


def players_transaction(players):
    print("\n=== Transaction: Alice gives Bob 2 potions ===")

    alice_potions_qty = players["alice"]["potion"].get("quantity")
    bob_potions_qty = players["bob"]["potion"].get("quantity")

    if alice_potions_qty >= 2:
        players["alice"]["potion"].update(quantity=alice_potions_qty - 2)
        players["bob"]["potion"].update(quantity=bob_potions_qty + 2)
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {players['alice']['potion']['quantity']}")
    print(f"Bob potions: {players['bob']['potion']['quantity']}")


def count_investory_items(inventory):
    inventory_value = 0
    item_count = 0

    for keys, values in inventory.items():
        inventory_value += (values.get("value") * values.get("quantity"))
        item_count += values.get("quantity")

    return inventory_value, item_count


def inventory_analytics(players):
    print("\n=== Inventory Analytics ===")

    most_value = 0
    most_value_player = ""

    most_items = 0
    most_items_player = ""

    rare_items = []

    for player_name, inventory in players.items():
        player_value, player_items = count_investory_items(inventory)

        if player_value > most_value:
            most_value = player_value
            most_value_player = player_name

        if player_items > most_items:
            most_items = player_items
            most_items_player = player_name

        for item_name, info in inventory.items():
            if info.get("rarity") == "rare":
                if item_name not in rare_items:
                    rare_items.append(item_name)

    print(f"Most valuable player: {most_value_player.capitalize()}"
          f"({most_value} gold)")
    print(f"Most items: {most_items_player.capitalize()} ({most_items} items)")

    print("Rarest items: ", end="")
    first = True
    for item in rare_items:
        if first is False:
            print(", ", end="")
        print(item, end="")
        first = False
    print()


def main():
    alice_inventory = {
        "sword": {
            "type": "weapon", "rarity": "rare",
            "quantity": 1, "value": 500
        },
        "potion": {
            "type": "consumable", "rarity": "common",
            "quantity": 5, "value": 50
        },
        "shield": {
            "type": "armor", "rarity": "uncommon",
            "quantity": 1, "value": 200
        }
    }
    bob_inventory = {
        "potion": {
            "type": "consumable", "rarity": "common",
            "quantity": 0, "value": 50
        },
    }
    players = {
        "alice": alice_inventory,
        "bob": bob_inventory
    }

    player_inventory(players)
    players_transaction(players)
    inventory_analytics(players)


if __name__ == "__main__":
    main()
