from aoc import day4

'''
However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

    112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
    123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
    111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
'''


def test_is_increasing():
    assert day4.is_increasing('111111')
    assert day4.is_increasing('223450') is False
    assert day4.is_increasing('123789')
    
def test_has_double():
    assert day4.has_double('111111') is False
    assert day4.has_double('223450')
    assert day4.has_double('123789') is False
    assert day4.has_double('123444') is False
    assert day4.has_double('124444') is False
    assert day4.has_double('113222')
