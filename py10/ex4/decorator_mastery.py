import time
from functools import wraps

def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        duration = end - start
        print(f"Spell completed in {duration:.3f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(self, spell_name, power, *args, **kwargs):
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... (attempt {attempt}/{max_attempts})"
                            )
                    else:
                        return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball():
    time.sleep(0.1)
    return "Fireball cast!"


def main():

    print("\nTesting spell timer...")
    result = fireball()
    print(f"Result: {result}")
    print()

    print("Testing MageGuild...")
    guild = MageGuild()

    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("A1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()