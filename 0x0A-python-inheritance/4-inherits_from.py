#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """Method that determines if an object is a true subclass."""
    return False if type(obj) is a_class else isinstance(obj, a_class)
