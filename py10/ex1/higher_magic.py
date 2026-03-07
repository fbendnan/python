def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)

    return combined


def fireball(x):
    return x * 10

def heal(x):
    return x + 20

def main():
    combined = spell_combiner(fireball, heal)

    print(combined(5))

main()