#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for Assignment 1 Part 1"""


def listDivide(numbers, divide=2):
    """A function returns the number of integer
    that are divisible by chosen number.

    Args:
        numbers (list): A list if ints
        divide (int, default = 2):divisor

    Returns:
        listlen (int): Length of list

    Example:
        listDivide([2, 4, 6, 8, 10])
        >>> 5
    """
    divisible = []
    for number in numbers:
        if (int(number) % int(divide)) == 0:
            divisible.append(number)
    listlen = len(divisible)
    return listlen


class ListDivideException(Exception):
    """Exception class"""
    pass


def testListDivide():
    """A function to test the listDivide function."""

    result = listDivide([1, 2, 3, 4, 5])
    if result != 2:
        raise ListDivideException("Caught Exception!")
    result = listDivide([2, 4, 6, 8, 10])
    if result != 5:
        raise ListDivideException("Caught Exception!")
    result = listDivide([30, 54, 63, 98, 100], divide=10)
    if result != 2:
        raise ListDivideException("Caught Exception!")
    result = listDivide([])
    if result != 0:
        raise ListDivideException("Caught Exception!")
    result = listDivide([1, 2, 3, 4, 5], 1)
    if result != 5:
        raise ListDivideException("Caught Exception!")


testListDivide()
