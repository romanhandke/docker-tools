import click
import os
import subprocess

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')


class DockerTools(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns[name]


class DockerContainerList:
    def __init__(self):
        result = subprocess.run([
            "docker container ls -a --format '{{.ID}};{{.Names}};{{.Status}}'"
        ],
                                stdout=subprocess.PIPE,
                                shell=True,
                                check=True)

        container_strings = result.stdout.decode('utf-8').splitlines()

        self.containers = []
        for string in container_strings:
            values = string.split(';')
            self.containers.append({
                'id': values[0],
                'name': values[1],
                'status': 'Up' in values[2]
            })


@click.group(cls=DockerTools, help='A collection of docker related scripts')
@click.pass_context
def cli(ctx):
    ctx.obj = DockerContainerList()


if __name__ == '__main__':
    cli()
