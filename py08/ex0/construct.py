import os
import sys
import site


def is_env():
    return hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix

def main():
    if is_env():
        print("MATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system")
        print()
        print(f"Package installation path: {site.getsitepackages()[0]}")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!"
              "\nThe machines can see everything you install.")
        print()
        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\n"
              "Scripts\n"
              "activate   # On Windows\n"
              "Then run this program again.")
        print()
        print("Then run this program again.")

main()
