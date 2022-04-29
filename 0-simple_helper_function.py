#!/usr/bin/env python3
""" Write a function named index_range that takes
two integer arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of the start and end index of the page
    """
    start = page (page - 1) * page_size
    end = start + page_size
    return start, end