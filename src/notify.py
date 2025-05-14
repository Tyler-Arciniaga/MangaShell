import click

@click.command()
def notify():
    '''Open notifications menu so you never miss another release!'''
    click.echo("Opening notify menu!")