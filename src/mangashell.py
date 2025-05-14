import click
import add
import update
import log
import notify


@click.group()
def mangashell():
    """Welcome to MangaShell!
    Tired of bloated trackers? MangaShell lets you effortlessly track all your favorite anime and manga, right from the terminal.
    """

mangashell.add_command(add.add)
mangashell.add_command(update.update)
mangashell.add_command(log.log)
mangashell.add_command(notify.notify)