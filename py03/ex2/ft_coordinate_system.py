import math

def distance_3d(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)


def parse_coords(s):
    parts = s.split(",")
    return tuple(int(p) for p in parts)
        
    
def check_tup_len_error(tup_pos):
    tup_len = 0
    for i in tup_pos:
        tup_len += 1
    if tup_len != 3:
        raise LenError("you must create 3 cordinates x, y and z")
        

class LenError(Exception):
    pass
    

def main():
    print("=== Game Coordinate System ===")

    base_c = (0, 0, 0)
    created = (44, -15, -10)
    try:
        print(f"Position created: {created}")
        check_tup_len_error(created)
        print(f"Distance between {base_c} and {created}: {distance_3d(base_c, created):.2f}")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    s = "3,4, 0"
    print(f'\nParsing coordinates: "{s}"')
    try:
        pos = parse_coords(s)
        print(f"Parsed position: {pos}")
        check_tup_len_error(pos)
        print(f"Distance between {base_c} and {pos}: {distance_3d(base_c, pos):.2f}")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return

    bad = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{bad}"')
    try:
        bad_pos = parse_coords(bad)
        check_tup_len_error(bad_pos)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
