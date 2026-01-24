def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name: str = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    file = open(file_name, 'w')
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    line1: str = "[ENTRY 001] New quantum algorithm discovered\n"
    line2: str = "[ENTRY 002] Efficiency increased by 347%\n"
    line3: str = "[ENTRY 003] Archived by Data Archivist trainee\n"
    lines = [line1, line2, line3]
    for line in lines:
        file.write(line)
        print(line, end="")
    print()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")
    file.close()


main()
