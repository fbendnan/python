def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        file_name: str = "ancient_fragment.txt"
        print(f"\nAccessing Storage Vault: {file_name}")
        file = open(file_name, 'r')
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(file.read())
    except Exception as e:
        print(f"Error: {e}")
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")


main()
