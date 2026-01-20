import sys
from typing import Dict


def find_index(str) -> int:
    i: int = 0
    for c in str:
        i += 1
        if c == ":":
            return i


def make_dict_from_list(inventories_list) -> Dict:
    my_dict: Dict = {}
    for str in inventories_list:
        i = find_index(str)
        key = str[: i - 1]
        value = int(str[i:])
        my_dict[key] = value
    return my_dict


def inventory_sys_analysis(inventories):
    print("=== Inventory System Analysis ===")
    total_items = 0
    for item, qty in inventories.items():
        total_items += qty
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventories)}")
    return total_items


def current_inventory(inventories, total_items):
    inventories = dict(
        sorted(inventories.items(), key=lambda item: item[1], reverse=True)
    )
    print("\n=== Current Inventory ===")
    for item, qty in inventories.items():
        per = (qty / total_items) * 100
        print(f"{item}: {qty} units ({per:.2f}%)")


def inventory_statics(inventories, total_items):
    print("\n=== Inventory Statistics ===")
    most = ""
    least = ""
    most_qty = 0
    least_qty = total_items
    for item, qty in inventories.items():
        if qty > most_qty:
            most = item
            most_qty = qty
        if qty <= least_qty:
            least = item
            least_qty = qty

    print(f"Least abundant: {least} ({least_qty} unit)")
    print(f"Most abundant: {most} ({most_qty} units)")


def lookup_in_dict(inventories, to_find):
    for item, qty in inventories.items():
        if item == to_find:
            return f"'{to_find}' in inventory: {True}"
    return f"'{to_find}' in inventory: {False}"


def management_sugg(inventories):
    print("\n=== Management Suggestions ===")
    restock_needed = []
    for item, qty in inventories.items():
        if qty < 2:
            restock_needed += [item]
    print(f"Restock needed: {restock_needed}")


def dict_properties(inventories):
    print("\n=== Dictionary Properties Demo ===")
    dict_keys = []
    dict_values = []
    for item, qty in inventories.items():
        dict_keys += [item]
        dict_values += [qty]
    print(f"Dictionary keys: {dict_keys}")
    print(f"Dictionary values: {dict_values}")
    sword_lookup = lookup_in_dict(inventories, 'sword')
    print(f"Sample lookup - {sword_lookup}")


# def sort_dict(inventories):
#     sort_dict = {}
#     i = 0
#     for item, qty in inventories.items():
#         for item, qty in inventories.items():
#             if qty >= i:
#                 sort_dict[item] = qty


def item_categories(inventories):
    print("\n=== Item Categories ===")
    Moderate_dict = {}
    Scarce_dict = {}
    for item, qty in inventories.items():
        if qty >= 5:
            Moderate_dict[item] = qty
        else:
            Scarce_dict[item] = qty

    print(f"Moderate: {Moderate_dict}")
    print(f"Scarce: {Scarce_dict}")


def main():
    tmp_inventories = sys.argv[1:]
    if len(tmp_inventories) != 0:
        try:
            inventories = make_dict_from_list(tmp_inventories)
            total_items = inventory_sys_analysis(inventories)
            current_inventory(inventories, total_items)
            inventory_statics(inventories, total_items)
            item_categories(inventories)
            management_sugg(inventories)
            dict_properties(inventories)
        except Exception:
            print(Exception)


main()
