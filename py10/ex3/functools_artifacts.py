from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Dict


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: Dict[str, Callable] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    op = operations.get(operation)
    if op is None:
        raise ValueError("Unsupported operation")

    return reduce(op, spells)


def enchanter(power, element, target):
    return f"{element} enchantment with power {power} on {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchant = partial(base_enchantment, 50, 'fire')
    ice_enchant = partial(base_enchantment, 50, 'ice')
    lightning_enchant = partial(base_enchantment, 50, 'lightning')

    return {
        'ice_enchant': ice_enchant('dragon'),
        'fire_enchant': fire_enchant('dragon'),
        'lightning_enchant': lightning_enchant('dragon')
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:

    @singledispatch
    def cast_spell(arg):
        return "Uknown data type"

    @cast_spell.register(int)
    def _(damage_spell):
        return f"Damage spell deals {damage_spell} HP"

    @cast_spell.register(str)
    def _(enchantment):
        return f"Enchants item with {enchantment}"

    @cast_spell.register(list)
    def _(spells):
        return f"Multi-cast spells: {', '.join(spells)}"

    return cast_spell


def main():
    spells = [14, 27, 35, 18, 42, 23]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting spell reducer...")
    partial_ench = partial_enchanter(enchanter)
    print(partial_ench)

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell_dispatcher...")
    spell_disp = spell_dispatcher()
    print(spell_disp(5))
    print(spell_disp("flamingo"))
    print(spell_disp(['1', '2', '4', '6']))


main()
