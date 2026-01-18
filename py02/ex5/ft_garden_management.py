class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class plant:
    def __init__(self, plant_name, water_level, sunlight_hours):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plants(self, plant):
        try:
            if plant.plant_name is None or plant.plant_name == "":
                raise PlantError("Error adding plant: Plant name "
                                 "cannot be empty!")
            self.plants += [plant]
            print(f"Added {plant.plant_name} successfully")
        except GardenError as e:
            print(e)

    def water_plants(self, water_lvl, should_lvl):
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                if water_lvl < should_lvl:
                    raise WaterError()
                print(f"Watering {plant.plant_name} - success")
        except GardenError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        print("\nChecking plant health...")
        for plant in self.plants:
            try:
                if plant is None or plant == "":
                    raise ValueError("Error: Plant name cannot be empty!")
                if plant.water_level > 10:
                    raise ValueError(f"Error checking {plant.plant_name}: "
                                     f"Water level {plant.water_level} "
                                     f"is too high (max 10)")
                elif plant.water_level < 1:
                    raise ValueError(f"Error checking {plant.plant_name}: "
                                     f"Water level {plant.water_level} "
                                     f"is too low (min 1)")
                if plant.sunlight_hours < 2:
                    raise ValueError(f"Error checking {plant.plant_name}: "
                                     f"Sunlight hours {plant.sunlight_hours} "
                                     f"is too low (min 2)")
                elif plant.sunlight_hours > 12:
                    raise ValueError(f"Error checking {plant.plant_name}: "
                                     f"Sunlight hours {plant.sunlight_hours} "
                                     f"is too high (max 12)")
                print(f"{plant.plant_name}: healthy (water: "
                      f"{plant.water_level}, sun: {plant.sunlight_hours})")
            except ValueError as e:
                print(e)


def test_garden_management():
    print("=== Garden Management System ===")
    garden_1 = GardenManager()
    print("\nAdding plants to garden...")
    garden_1.add_plants(plant("tomato", 5, 8))
    garden_1.add_plants(plant("lettuce", 15, 8))
    garden_1.add_plants(plant(None, 5, 8))
    garden_1.water_plants(2, 5)
    garden_1.check_plant_health()
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


test_garden_management()
