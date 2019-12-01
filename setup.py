from setuptools import setup

setup(
    name='AoC2019',
    version='1.0',
    description='Advent of Code 2019',
    author='Vance Morris',
    url='https://github.com/vmorris/Aoc2019',
    packages=['aoc'],
    include_package_data=True,
    py_modules=['aoc'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        aoc=aoc.aoc:cli
    ''',
)
