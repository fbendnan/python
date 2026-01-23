import sys

def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    # sys.stdout.write("hello world!\n")
    stdin1 = input("Input Stream active. Enter archivist ID: ")
    stdin2 = input("Input Stream active. Enter status report: ")

    stdout = sys.stdout
    stdout.write(f"\n[STANDARD] Archive status from {stdin1}: {stdin2}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
    stdout.write("[STANDARD] Data transmission complete\n")
    print()
    print("Three-channel communication test successful.")
    

main()