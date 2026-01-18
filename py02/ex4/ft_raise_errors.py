def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name is None or plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too low (min 1)")
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as ll:
        print(ll)


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    check_plant_health("tomato", 5, 8)
    print()
    print("Testing empty plant name...")
    check_plant_health("", 5, 8)
    print()
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 8)
    print()
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print()
    print("All error raising tests completed!")


test_plant_checks()
