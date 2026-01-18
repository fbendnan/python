class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_errors():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    plant_name = "Tomato"
    try:
        raise PlantError(f"Caught PlantError: The {plant_name} "
                         f"plant is wilting!")
    except PlantError as e:
        print(e)
    print("\nTesting WaterError...")
    try:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    except WaterError as e:
        print(e)

    print("\nTesting catching all garden errors...")
    try:
        raise (PlantError(f"Caught PlantError: The {plant_name} "
                          f"plant is wilting!"))
    except GardenError as e:
        print(e)
    try:
        raise (WaterError("Caught WaterError: Not enough water in the tank!"))
    except GardenError as e:
        print(e)


test_errors()
