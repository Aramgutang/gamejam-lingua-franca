class NoPathFound(Exception):
    pass

from .astar import astar, fstar
from .path import find_closest_path
