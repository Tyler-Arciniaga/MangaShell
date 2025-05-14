import click

@click.command()
def log():
    '''Browse your current log'''
    click.echo("Showing log")