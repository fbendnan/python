import sys


def main():
    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
        stdin1 = input("Input Stream active. Enter archivist ID: ")
        stdin2 = input("Input Stream active. Enter status report: ")
        print(f"\n[STANDARD] Archive status from {stdin1}: {stdin2}",
              file=sys.stdout)
        print("[ALERT] System diagnostic: Communication channels verified",
              file=sys.stderr)
        print("[STANDARD] Data transmission complete",
              file=sys.stdout)
        print()
        print("Three-channel communication test successful.")
    except Exception as e:
        print(f"Error : {e}")


main()
