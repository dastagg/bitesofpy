"""Use deepcopy to pass by value not reference."""

import copy

items = [
    {"id": 1, "name": "laptop", "value": 1000},
    {"id": 2, "name": "chair", "value": 300},
    {"id": 3, "name": "book", "value": 20},
]


def duplicate_items(c_items):
    return copy.deepcopy(c_items)
