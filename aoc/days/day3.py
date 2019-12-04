from collections import namedtuple
from itertools import product
from multiprocessing import Pool


Point = namedtuple('Point', ['x', 'y'])


class Line:
    def __init__(self, id, point1, point2):
        self.id = id
        self.point1 = point1
        self.point2 = point2
        self.points = self._points()
        
    def _points(self):
        points = []
        if self.point1.x == self.point2.x:
            # vertical line
            start = self.point1.y
            end = self.point2.y
            if self.point1.y < self.point2.y:
                for y in range(start, end + 1):
                    points.append(Point(self.point1.x, y))
            else:
                for y in range(start, end - 1, -1):
                    points.append(Point(self.point1.x, y))
                    
        elif self.point1.y == self.point2.y:
            # horizontal line
            start = self.point1.x
            end = self.point2.x
            if self.point1.x < self.point2.x:
                for x in range(start, end + 1):
                    points.append(Point(x, self.point1.y))
            else:
                for x in range(start, end - 1, -1):
                    points.append(Point(x, self.point1.y))
                    
        return points
        
    def intersection(self, other):
        if self.id != other.id:
            for point in self.points:
                if point in other.points and point != Point(0,0):
                    return point
        return None
    
    def __repr__(self):
        return f'{self.point1.x, self.point1.y}->{self.point2.x, self.point2.y}'


def get_points(wire_steps):
    points = [Point(0,0)]
    current_step = points[0]
    for step in wire_steps:
        direction = step[0]
        distance = int(step[1:])
        if direction == 'U':
            # pos Y
            next_step = Point(current_step.x, current_step.y + distance)
        elif direction == 'D':
            # neg Y
            next_step = Point(current_step.x, current_step.y - distance)
        elif direction == 'R':
            # pos X
            next_step = Point(current_step.x + distance, current_step.y)
        elif direction == 'L':
            # neg X
            next_step = Point(current_step.x - distance, current_step.y)
        points.append(next_step)
        current_step = next_step
    return points


def get_path(id, points):
    path = []
    current_point = points[0]
    for point in points[1:]:
        next_point = point
        path.append(Line(id, current_point, next_point))
        current_point = next_point
    return path


def steps_to_point(path, point):
    #print(f'Calculating path to {point}...')
    steps = 0
    points_seen = [ (Point(0,0), 0) ]  # (Point, distance)
    for line in path:
        #print(f'iterate: steps = {steps}')
        #print(line)
        for p in line.points[1:]:
            #print(p)
            steps += 1
            for seen in points_seen:
                if p == seen[0]:
                    #print(f'seen {p} already')
                    #print(f'resetting steps to: {seen[1]}')
                    steps = seen[1]
                    break
            points_seen.append( (p, steps) )
            if p == point:
                return steps


def paths_intersect(paths):
    return paths[0].intersection(paths[1])
    

def calculate_delay(args):
        return steps_to_point(args[0], args[2]) + steps_to_point(args[1], args[2])


def day3(data):
    with open(data, 'r') as f:
        wire1, wire2 =f.readlines()
        wire1_steps = wire1.split(',')
        wire2_steps = wire2.split(',')
    
    wire1_points = get_points(wire1_steps)
    wire2_points = get_points(wire2_steps)
    
    wire1_path = get_path('wire1', wire1_points)
    wire2_path = get_path('wire2', wire2_points)

    p = Pool(20)
    intersections = p.map(paths_intersect, list(product(wire1_path, wire2_path)))
    
    filtered = list(filter(None, intersections))
    
    distances = {}
    for point in filtered:
        distance = abs(point.x) + abs(point.y)
        distances[distance] = point
    
    shortest = min(distances.keys())
    print(shortest, distances[shortest])

    to_calc = []
    for f in filtered:
        to_calc.append((wire1_path, wire2_path, f))

    delays = p.map(calculate_delay, to_calc)
        
    print(min(delays))
    