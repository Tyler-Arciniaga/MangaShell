import click
import time
from mongo import entries, userID
from richConsole import console

@click.command()
@click.option("-c", "--chapter", default = None, type = int)
@click.option("-r", "--rating", default = None, type = int)
@click.option("-s", "--status", default=None, help="completed, oon-hold, dropped, plan-to-read")
@click.argument('title', nargs=-1)
def update(title: str, chapter: int, rating: int, status: str):
    '''Update manga information in your log'''
    
    rawTitle = " ".join(title)
    entryTitle = rawTitle.title()
    entry = entries.find_one({"title": entryTitle, "userID": userID})
    entryID = entry['_id']

    if not entry:
        console.print(f"[error]Could not find [underline]{rawTitle}[/underline] in your log, perhaps check spelling or add to log first")
        return 0

    if not chapter and not rating and not status:
        console.print("[error]Please specify option(s) for what you wish to update for this specific entry")
        console.print("Currently your log show:")
        console.print(f"[emphasize]{entryTitle}[/emphasize]")
        console.print(f"chapter: [cyan]{chapter}[/cyan]")
        console.print(f"rating: [yellow]{rating}[/yellow]")
        console.print(f"status: [purple]{status}[/purple]")

    #handle incorrect status input
    if status and status.lower() not in ("completed", "on-hold", "dropped", "plan-to-read"):
        console.print("[error]status must be one of: completed, on-hold, dropped, plan-to-read")
        return 0
    
    with console.status(f"Updating [emphasize]{entryTitle}[/emphasize] in your log...", spinner = 'clock'):
        time.sleep(1)
        try:
            result = entries.update_one({'_id': entryID}, {'$set' : {'chapter': chapter, 'rating': rating, 'status': status}})
        except Exception as e:
            console.print(f"[error]Whoops! Error updating entry in your log: {e}")
            return 0
        else:
            console.print(f"[green]👍 Successfully updated [emphasize]{entryTitle}[/emphasize] in your log")
        
        

