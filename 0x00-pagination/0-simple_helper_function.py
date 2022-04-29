#!/usr/bin/env python3
"""
This is a simple helper function to find
start and end pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return the start and end index of the range
    of items to be displayed on the page.
    Args:
        page (int): The page number.
        page_size (int): The number of items per page.
    Returns:
        tuple: The start and end index of the range
        of items to be displayed on the page.
    """
    end = page * page_size
    start = end - page_size
    return start, end