def garden_operations(error, is_one_error):
    if is_one_error:
        try:
            if error == "ValueError":
                int("abc")
            elif error == "ZeroDivisionError":
                result = 4/0
                print(result)
            elif error == "FileNotFoundError":
                open("missing.txt", "r")
            elif error == "KeyError":
                d = {}
                print(d["plant"])
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    errors = ["ValueError", "ZeroDivisionError", "FileNotFoundError",
              "KeyError"]

    for error in errors:
        print(f"\nTesting {error}...")
        garden_operations(error, True)
    print("\nTesting multiple errors together...")
    try:
        result = 4/0
        print(result)
        d = {}
        print(d["plant"])
        file = open("missing.txt", "r")
        file.close()
    except Exception:
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


test_error_types()
