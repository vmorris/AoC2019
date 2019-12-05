from setuptools import setup, find_packages

setup(
    name = 'AoC2019',
    version = '1.0',
    description = 'Advent of Code 2019',
    author = 'Vance Morris',
    url = 'https://github.com/vmorris/Aoc2019',
    packages = find_packages(),
    install_requires = [
    'pytest'
    ],
    include_package_data = True,
    py_modules = [
        'aoc'
    ],
)
