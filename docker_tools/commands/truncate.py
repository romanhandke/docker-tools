import click
import inquirer
import subprocess


@click.command()
@click.pass_context
def truncate(ctx):
    """Truncate log files of containers"""
    containers = []
    for container in ctx.obj.containers:
        containers.append(container['name'])

    questions = [
        inquirer.Checkbox(
            'containers',
            message="Which containers' log files do you want to truncate?",
            choices=containers),
    ]
    answers = inquirer.prompt(questions)

    for container_name in answers['containers']:
        command = "sudo truncate -s 0 $(docker inspect --format='{{.LogPath}}' %s)" % container_name
        subprocess.run(command, stdout=subprocess.PIPE, shell=True, check=True)
