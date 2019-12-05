from aoc import day1

def test_calculate_fuel_no_recalc():
    test_data = [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
    ]
    for mass, fuel in test_data:
        assert day1.calculate_fuel(mass, recalc_for_fuel=False) == fuel
        
def test_calculate_fuel_recalc():
    test_data = [
        (14, 2),
        (1969, 966),
        (100756, 50346)
    ]
    for mass, fuel in test_data:
        assert day1.calculate_fuel(mass, recalc_for_fuel=True) == fuel
