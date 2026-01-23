def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        file_name = "ancient_fragment.txt"
        print(f"\nAccessing Storage Vault: {file_name}")
        file = open(file_name, 'r')
        print("Connection established...\n")
        for line in file:
            print(line)
        file.close()
    except Exception as e:
        print(f"Error: {e}")

main()