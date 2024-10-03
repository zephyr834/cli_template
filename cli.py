import click
import importlib.metadata

package_version = importlib.metadata.version('myapp')

@click.group()
@click.version_option(package_version, prog_name="myapp")
@click.group()
@click.version_option(version='1.0.0')
def cli():
    "Cli Template"

@cli.command(name="command")
@click.argument("myArgument")
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(myArgument, option):
    "Command description goes here"
    click.echo("Here is some output")