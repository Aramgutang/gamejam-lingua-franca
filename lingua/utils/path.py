from itertools import count

from numpy import array, pi, sin, cos, ceil

from . import NoPathFound

def find_closest_path(target, levels):
    for radius in count(1):
        found = check_radius(radius, array(target), levels)
        if found is not None:
            return found
        if radius > max(levels.shape):
            raise NoPathFound()

DIRECTIONS = array([[1,1],[-1,1],[-1,-1],[1,-1]])

def check_radius(radius, target, levels):
    sections = 4.0*(radius+1.0)
    increment = 2*pi/sections
    for theta in range(0,sections):
        x = ceil(target[0] + radius * cos(theta * increment))
        y = ceil(target[1] + radius * sin(theta * increment))
        try:
            if levels[x,y]:
                return (x,y)
        except IndexError:
            pass
    return None