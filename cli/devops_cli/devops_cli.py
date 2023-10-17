import click

@click.group()
def cli():
    pass

@cli.command("disk_sdk", short_help="Show Disk information usind SDK")

def disk_sdk():
    click.echo()

@cli.command("disk_cmd", short_help="Show Disk information")

def disk_cmd():
    click.echo(subprocess.run(["df","-h"]))