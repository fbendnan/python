#!/usr/bin/env python3
import sys


def print_arguments(len_arg: int, arguments: list[str]) -> None:
    print(f"Arguments received: {len_arg - 1}")
    i: int = 1
    for arg in arguments[1:]:
        print(f"Argument {i}: {arg}")
        i += 1


def main() -> None:
    arguments: list[str] = sys.argv
    len_arg: int = len(arguments)
    print("=== Command Quest ===")
    if len_arg == 1:
        print("No arguments provided!")
    print(f"Program name: {arguments[0]}")
    if len_arg > 1:
        print_arguments(len_arg, arguments)
    print(f"Total arguments: {len_arg}")


if __name__ == "__main__":
    main()
