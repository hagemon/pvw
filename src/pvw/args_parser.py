from pvw.env import EnvironmentManager
from pvw.config import config

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
    remove an existing venv
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
    activate a venv, using `source pvw actvate env` or `source pvw env` in Unix, `pvw activate env` or `pvw env` in Windows
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
