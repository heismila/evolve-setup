"""A simple greeting script that takes a name as a command-line argument."""

import sys


def greet(name: str) -> str:
    """Return a personalised greeting for the given name."""
    return f"Hello, {name}! Welcome to your professional development environment."


def main() -> None:
    """Run the greeting from the command line."""
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(greet(name))
    else:
        print("Usage: python greet.py <name>")


if __name__ == "__main__":
    main()