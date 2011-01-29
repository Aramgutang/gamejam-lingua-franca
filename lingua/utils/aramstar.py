from math import sqrt

class NoPathFound(Exception):
    pass

def directions(dx, dy):
    """
    Returns the optimal order of directions to search in.
    Comments assume (1,1) is North-East.
    """
    if abs(dy*2) > abs(dx):
        if dy > 0:
            if dx > 0:
                return [(0,-1),(-1,-1),(1,-1),(-1,0),(1,0),(-1,1),(1,1),(0,1)] #NNE
            else:
                return [(0,-1),(1,-1),(-1,-1),(1,0),(-1,0),(1,1),(-1,1),(0,1)] #NNW
        else:
            if dx > 0:
                return [(0,1),(-1,1),(1,1),(-1,0),(1,0),(-1,-1),(1,-1),(0,-1)] #SSE
            else:
                return [(0,1),(1,1),(-1,1),(1,0),(-1,0),(1,-1),(-1,-1),(0,-1)] #SSW
    elif abs(dx) < abs(dy):
        if dy > 0:
            if dx > 0:
                return [(-1,-1),(0,-1),(-1,0),(1,-1),(-1,1),(1,0),(0,1),(1,1)] #NEE
            else:
                return [(1,-1),(0,-1),(1,0),(-1,-1),(1,1),(-1,0),(0,1),(-1,1)] #NWW
        else:
            if dx > 0:
                return [(-1,1),(0,1),(-1,0),(1,1),(-1,-1),(1,0),(0,-1),(1,-1)] #SEE
            else:
                return [(1,1),(0,1),(1,0),(-1,1),(1,-1),(-1,0),(0,-1),(-1,-1)] #SWW
    elif abs(dy*2) > abs(dy):
        if dy > 0:
            if dx > 0:
                return [(-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,-1),(1,1),(1,0)] #EEN
            else:
                return [(1,0),(1,-1),(1,1),(0,-1),(0,1),(-1,-1),(-1,1),(-1,0)] #WWN
        else:
            if dx > 0:
                return [(-1,0),(-1,1),(-1,-1),(0,1),(0,-1),(1,1),(1,-1),(1,0)] #EES
            else:
                return [(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,1),(-1,-1),(-1,0)] #WWS
    else:
        if dy > 0:
            if dx > 0:
                return [(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(0,1),(1,0),(1,1)] #ENN
            else:
                return [(1,-1),(1,0),(0,-1),(1,1),(-1,-1),(0,1),(-1,0),(-1,1)] #WNN
        else:
            if dx > 0:
                return [(-1,1),(-1,0),(0,1),(-1,-1),(1,1),(0,-1),(1,0),(1,-1)] #ESS
            else:
                return [(1,1),(1,0),(0,1),(1,-1),(-1,1),(0,-1),(-1,0),(-1,-1)] #WSS

def traversable(levels, x, y,):
    return x >= 0 and x < levels.shape[0] and y >= 0 and y < levels.shape[1] and levels[x,y]

class Node(object):
    def __init__(self, start, end, levels, length=0, parent=None):
        self.start = start
        self.end = end
        self.dx = end[0] - start[0]
        self.dy = end[1] - start[1]
        self.directions = directions(self.dx, self.dy)
        self.length = length
        self.levels = levels
        self.parent = parent
    
    def __cmp__(self, other):
        return cmp(self.heuristic(), other.heuristic())
    
    def __eq__(self, other):
        return self.start == other.start
    
    def heuristic(self):
        if not hasattr(self, '_heuristic'):
            #self._heuristic = self.length + sqrt(self.dx**2 + self.dy**2)
            self._heuristic = self.length + abs(self.dx) + abs(self.dy)
        return self._heuristic
    
    def next(self):
        while self.directions:
            dx, dy = self.directions.pop()
            new_position = (self.start[0]+dx, self.start[1]+dy)
            if traversable(self.levels, *new_position):
                #increment = 1.0 if dx == 0 or dy == 0 else 1.41
                yield Node(new_position, self.end, self.levels, self.length + 1, self)
    
    def path(self):
        return [self.start,] + (self.parent.path() if self.parent else [])

def aramstar(start, end, levels):
    if not traversable(levels, *start) or not traversable(levels, *end):
        return []
    open = [Node(start, end, levels),]
    closed = []
    while open:
        node = open.pop()
        closed.append(node)
        if node.start == end:
            return node.path()
        for next in node.next():
            if next not in open and next not in closed:
                open.append(next)
                if len(open) > 1 and next > open[-2]:
                    open.sort(reverse=True)
    raise NoPathFound()
    
        