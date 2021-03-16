import click
from rich.console import Console
from rich.table import Table
import fontawesome as fa


@click.command()
@click.pass_context
@click.option('--up', is_flag=True, help="Show only running containers")
def status(ctx, up):
    '''Show an abbreviated status for all containers'''
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("id", style="dim", width=12)
    table.add_column("name")
    table.add_column("status")
    for container in ctx.obj.containers:
        if container['status'] is False:
            if up:
                continue

            container['status'] = "[red]" + fa.icons['arrow-down'] + "[/red]"

        if container['status'] is True:
            container['status'] = "[green]" + \
                fa.icons['arrow-up'] + "[/green]"

        table.add_row(container['id'], container['name'], container['status'])

    console.print(table)
