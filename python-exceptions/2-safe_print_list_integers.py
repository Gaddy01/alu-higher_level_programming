#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counts the number of integers printed
    for i in range(x):
        try:
            # Attempt to print only integers
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip if the element is not an integer
            continue
        except IndexError:
            # Stop if we go out of range
            break
    print()  # New line after printing all integers
    return count
