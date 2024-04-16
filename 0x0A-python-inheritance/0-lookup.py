#!/usr/bin/python3

"""Defiine an object function lookup."""


def lookup(obj):
    """Looks up object, returns its list of attributes and methods"""
    return (dir(obj))
