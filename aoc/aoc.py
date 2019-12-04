import configparser
import click
import os

from aoc.cli.commands import *
from aoc.util.config import Config


class AoC:
    def __init__(self):
        self.config = Config().read_config()


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = AoC()


[cli.add_command(day) for day in [
    day1,
    day2,
    day3,
]]
