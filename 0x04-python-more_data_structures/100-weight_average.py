#!/usr/bin/python3
"""Model that calculate the weighted average of all integers tuple"""


def weight_average(my_list=[]):
    """Function that return the weighted average of all integer tuple"""
    if not my_list:  # Check if the list is empty
        return 0

    total_weighted_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_score += score * weight
        total_weight += weight

    # Avoid division by zero (though weights being 0 is unlikely given the problem)
    if total_weight == 0:
        return 0

    return total_weighted_score / total_weight
