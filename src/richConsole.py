from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "emphasize": "bold underline magenta",
    "error": "bold red"
})

console = Console(theme=custom_theme)