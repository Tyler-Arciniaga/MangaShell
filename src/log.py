import click
import time
from mongo import entries, userID
from richConsole import console
from rich.table import Table

@click.option("-f", "--find", default = None, help = "Query a specific title")
@click.command()
def log(find: str):
    '''Browse your current log'''
    if (find):
        
        entryTitle = (find).title()  #handle multi-word titles and clean up so that only one variation exists
        with console.status(f"Find [emphasize]{entryTitle}[/emphasize] in your log...", spinner = 'monkey'):
            time.sleep(1)
            console.print(f"Finding {entryTitle} in your logs...")
            try:
                queryRes = entries.find_one({"title": entryTitle, "userID": userID})
        
                if queryRes:
                    console.print(f"Current Log Info on: [emphasize]{entryTitle}[/emphasize]")
                    if queryRes['chapter']:
                        console.print(f"chapter: {queryRes['chapter']}")
                    if queryRes['rating']:
                        console.print(f"rating: [yellow]{queryRes['rating']}[/yellow]")
                    if queryRes['status']:
                        console.print(f"status: [purple]{queryRes['status']}[/purple]")
                else:
                    console.print(f"🙈 Looks like we couldn't find [emphasize]{entryTitle}[/emphasize] in your log...")
            except Exception as e:
                console.print(f"[error] Whoops! An error has occured: {e}[/error]")
                return 0

    
    else:
        with console.status(f"Fetching your log...", spinner = 'clock'):
            time.sleep(2)
            cursor = entries.find({"userID": userID})
            table = Table (title = "Your Log")
            table.add_column("Title", style = "cyan")
            table.add_column("Chapter", style = "magenta")
            table.add_column("Status", style= "red")
            table.add_column("Rating", style = "green")
            for doc in cursor:
                docChapter = str(doc['chapter']) if doc['chapter'] else "N/A"
                docStatus = doc['status'] if doc['status'] else "N/A"
                docRating = f"{str(doc['rating'])}/10" if doc['rating'] else "N/A"
                table.add_row(doc['title'], docChapter, docStatus, docRating)
            console.print(table)
