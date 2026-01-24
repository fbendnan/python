def checkfiles(file_name: str):
    try:
        with open(file_name, 'r') as file:
            print(f"\nROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except Exception as e:
        print(f"\nError: {e}")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    files_name = ["lost_archive.txt", "classified_vault.txt",
                  "standard_archive.txt"]
    for file_name in files_name:
        checkfiles(file_name)
    print("\nAll crisis scenarios handled successfully. Archives secure.")


main()
