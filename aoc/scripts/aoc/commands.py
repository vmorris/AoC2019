import os
import click
import aoc.days

    
@click.command()
@click.pass_context
def day1(ctx):
    data_file = os.path.join(
        ctx.obj.config.get('DEFAULT', 'data_dir'), 'day1.input'
    )
    aoc.days.day1.day1(data_file)


@click.command()
@click.pass_context
def day2(ctx):
    data_file = os.path.join(
        ctx.obj.config.get('DEFAULT', 'data_dir'), 'day2.input'
    )
    aoc.days.day2.day2(data_file)
