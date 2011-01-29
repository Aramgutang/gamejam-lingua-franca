from subprocess import Popen, PIPE

class NoPathFound(Exception):
    pass

#from .astar import astar, fstar
from .path import find_closest_path

def astar(start, end, levels):
    return list(reversed(eval(Popen("AStar.exe %s %s %s %s" % (start+end), stdout=PIPE, shell=True).stdout.read())))