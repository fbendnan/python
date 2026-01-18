def check_temperature(temp_str):
    try:
        temp_str = int(temp_str)
        if temp_str >= 0 and temp_str <= 40:
            print(f"Temperature {temp_str}°C is perfect for plants!")
        elif temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    temps = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    for temp in temps:
        print(f"\nTesting temperature: {temp}")
        check_temperature(temp)
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
