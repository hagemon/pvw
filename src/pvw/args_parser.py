from pvw.env import EnvironmentManager
from pvw.config import config
from pvw.template import Template
import os
import click

_env_manager = EnvironmentManager()


@click.group
@click.version_option()
def pvw():
    pass


@pvw.command
@click.option(
    "-s",
    "--show-size",
    default=False,
    is_flag=True,
    help="whether show sizes of each venv, this operation could take a while.",
)
def ls(show_size):
    """
    list all venvs.
    """
    if show_size:
        _env_manager.read_size()
    _env_manager.show()


@pvw.command()
@click.argument("name")
def create(name):
    """
    create a new venv
    """
    _env_manager.create(name=name)


@pvw.command()
@click.argument("names", nargs=-1)
def rm(names):
    """
<<<<<<< HEAD
    remove existing venvs, you can pass mutiple names with regular expression.
=======
    remove an existing venv
>>>>>>> 7e50aab6fa78c983fa2913c5f40026ce440c5cc6
    """
    _env_manager.remove(names=names)


@pvw.command()
@click.argument("name")
@click.option(
    "--shorten",
    hidden=True,
    is_flag=True,
    help="whether using a shorten stype for activating envs. (hidden option)",
)
def activate(name, shorten):
    """
    activate a venv. (additional `source` command is needed in Linux/MacOS)
    """
    try:
        _env_manager.activate(name=name)
    except NameError as e:
        if shorten:
            ctx = pvw.make_context("pvw", [name])
            with ctx:
                pvw.invoke(ctx)
        else:
            click.echo(e)


@pvw.command()
@click.argument("name")
def init(name):
    """
    start a new project with default template
    """
    try:
        path = os.path.join(os.getcwd(), name)
        template = Template(name=name, path=path)
        template.build()
        is_create_venv = click.confirm(
            "Do you want to create a new venv for this project?", default=True
        )
        if is_create_venv:
            venv_name = input(f"Enter the name of venv ({name})")
            if not venv_name:
                venv_name = name
            _env_manager.create(os.path.join(path, name))
    except Exception as e:
        print(e)


@pvw.command()
@click.argument("src")
@click.argument("dest")
def mv(src, dest):
    """
    move (or rename) venv `src` to `dest`
    """
    _env_manager.move(source=src, target=dest)


@pvw.command()
@click.argument("src")
@click.argument("dest")
def cp(src, dest):
    """
    copy venv `src` to `dest`
    """
    _env_manager.copy(source=src, target=dest)


@pvw.group(name="config")
def config_cli():
    """get or set variables in config"""
    pass


@config_cli.command
@click.argument("name")
@click.argument("value")
def set(name, value):
    """
    set config options, including `venv_path`.
    """
    if name == "venv_path":
        config.set(name, value)


@config_cli.command
@click.argument("name")
def get(name):
    """
    get config options, including `venv_path`
    """
    if name == "venv_path":
        path = config.get(name)
        click.echo(path)


def parse():
    pvw(prog_name="pvw")


if __name__ == "__main__":
    parse()
