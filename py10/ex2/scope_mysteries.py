###ghoster__nonlocal

def mage_counter() -> callable:
    count = 0  # local variable captured by closure

    def counter():
        nonlocal count  # allow modifying count
        count += 1
        return count

    return counter

def main():
    ...