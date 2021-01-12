import click
from rich.console import Console
from rich.table import Table


@click.command()
@click.pass_context
def status(ctx):
    '''Show an abbreviated status for all containers'''
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("id", style="dim", width=12)
    table.add_column("name")
    table.add_column("status")
    for container in ctx.obj.containers:
        if container['status'] is False:
            container['status'] = "[red]Down[/red]"

        if container['status'] is True:
            container['status'] = "[green]Up[/green]"

        table.add_row(container['id'], container['name'], container['status'])

    console.print(table)
