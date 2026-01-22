import math


def distance_3d(a: tuple, b: tuple) -> float:
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


def parse_coords(s: str) -> tuple:
    x, y, z = (int(p) for p in s.split(","))
    return x, y, z


def check_tup_len_error(tup_pos: tuple) -> None:
    tup_len = 0
    for i in tup_pos:
        tup_len += 1
    if tup_len != 3:
        raise LenError("you must create 3 cordinates x, y and z")


class LenError(Exception):
    pass


def main() -> None:
    print("=== Game Coordinate System ===\n")

    base_c: tuple = (0, 0, 0)
    created: tuple = (44, 5, -10)
    try:
        print(f"Position created: {created}")
        check_tup_len_error(created)
        print(f"Distance between {base_c} and {created}: "
              f"{distance_3d(base_c, created):.2f}")
        s: str = "3,4, 0"
        print(f'\nParsing coordinates: "{s}"')
        pos: tuple = parse_coords(s)
        print(f"Parsed position: {pos}")
        check_tup_len_error(pos)
        print(f"Distance between {base_c} and {pos}: "
              f"{distance_3d(base_c, pos):.2f}")
        
        bad: str = "abc,def,ghi"
        print(f'\nParsing invalid coordinates: "{bad}"')
        bad_pos: tuple = parse_coords(bad)
        check_tup_len_error(bad_pos)
        print("\nUnpacking demonstration:")
        x: int
        y: int
        z: int
        x, y, z = pos
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


main()
