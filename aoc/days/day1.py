import math


def calculate_fuel(mass, recalc_for_fuel=False):
    fuel = 0
    to_add = math.floor(mass / 3) - 2
    if not recalc_for_fuel:
        fuel += to_add
    else:
        while to_add > 0:
            fuel += to_add
            to_add = math.floor(to_add / 3) - 2
    return fuel


def day1(data):
    with open(data, 'r') as f:
        modules = f.readlines()
    result = 0
    for m in modules:
        result += calculate_fuel(int(m), recalc_for_fuel=False)
    print(f'Part One: {result}')
    result = 0
    for m in modules:
        result += calculate_fuel(int(m), recalc_for_fuel=True)
    print(f'Part Two: {result}')
