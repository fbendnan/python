def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        return result * multiplier

    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return 'Spell fizzled'
    
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def caster(*args, **kwargs):
        results = []

        for spell in spells:
            result = spell(*args, **kwargs)
            results.append(result)

        return results

    return caster


def fireball(x):
    return x * 10


def heal(x):
    return x + 20


def is_enough_mana(mana):
    return mana >= 10


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined(1)
    print(f"Combined spell result: {result}")
    print()

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball(1)}, Amplified: {mega_fireball(1)}")
    print()

    print("Testing conditional caster...")
    safe_fireball = conditional_caster(is_enough_mana, fireball)
    print(f"With enough mana: {safe_fireball(15)}")
    print(f"Without enough mana: {safe_fireball(5)}")
    print()

    print("Testing spell sequence...")
    combo = spell_sequence([fireball, heal])
    print(f"Sequence result: {combo(6)}")


if __name__ == "__main__":
    main()
