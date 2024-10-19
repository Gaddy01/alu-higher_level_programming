#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter out names that start with '__'
    filtered_names = [name for name in names if not name.startswith('__')]

    # Sort and print the filtered names
    for name in sorted(filtered_names):
        print(name)
