"""
This is the __init__ file for board module.
"""

DIRECTION_MAP = {
    'W': (-1, 0),
    'S': (1, 0),
    'D': (0, 1),
    'A': (0, -1)
}

LOCATION_PREFIX = {
    'Kitchen': 'in the',
    'Grocery Store': 'in the',
    'Market': 'in the',
    'Destination': 'at',
    'Street': 'on the'
}