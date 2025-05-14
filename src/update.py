import click
from mongo import entries, userID

@click.command()
def update():
    '''Update manga information in your log'''
    click.echo("Updating!")