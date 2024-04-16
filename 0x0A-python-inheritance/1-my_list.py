#!/usr/bin/python3

"""Module for MyList class."""


class MyList(list):
    """Custom MyList class."""

    def print_sorted(self):
        """Method for printing sorted list in ascending order."""
        print(sorted(self))
