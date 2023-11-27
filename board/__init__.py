"""
This is the __init__ file for board module.
"""

DIRECTION_MAP = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

LOCATION_PREFIX = {
    'Kitchen': 'in the',
    'Grocery Store': 'in the',
    'Market': 'in the',
    'Destination': 'at',
    'Street': 'on the'
}