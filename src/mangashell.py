import click
import add
import update
import log
import notify


@click.group()
def mangashell():
    """Welcome to MangaShell!"""

mangashell.add_command(add.add)
mangashell.add_command(update.update)
mangashell.add_command(log.log)
mangashell.add_command(notify.notify)