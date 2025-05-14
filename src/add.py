import click
import time
from mongo import entries, userID
from richConsole import console

@click.command()
@click.option("-c", "--chapter", default = None, type = int) #create chapter metadate option with default 1 (so Click infers option arguement as int)
@click.option("-r", "--rating", default = None, type = int)
@click.option("-s", "--status", default=None, help="completed, oon-hold, dropped, plan-to-read")
@click.argument('entry', nargs=-1)
def add(entry: str, chapter: int, rating: int, status: str):
    """Add a new manga to your log"""

    entryTitle = (" ".join(entry)).title() #handle multi-word titles and clean up so that only one variation exists
    newDocument = {"userID": userID, "title": entryTitle, "chapter": chapter, "rating": rating, "status": status}

    if status and status.lower() not in ("completed", "on-hold", "dropped", "plan-to-read"):
        console.print("[error]status must be one of: completed, on-hold, dropped, plan-to-read")
        return 0
    with console.status(f"Adding [emphasize]{entryTitle}[/emphasize] to your log...", spinner = 'clock'):
        time.sleep(1) #fake delay, makes the terminal look cooler don't blame me...
        duplicate = entries.find_one({"userID": userID, "title": entryTitle})
        if duplicate:
            console.print(f"Seems you already [emphasize]{entryTitle}[/emphasize] in your log")
        else:
            try:
                entries.insert_one(newDocument)
            except Exception as e:
                console.print(f"[error] Uh oh an error has occured: {e}[/error]")
                return 0
            else:
                console.print(f"👍 [emphasize]{entryTitle}[/emphasize][green] was added to your logs![/green]")
                if (chapter or rating or status):
                    console.print("with:")
                    if chapter:
                        console.print(f"chapter: {chapter}")
                    if rating:
                        console.print(f"rating: [yellow]{rating}[/yellow]")
                    if status:
                        console.print(f"status: [purple]{status}[/purple]")


