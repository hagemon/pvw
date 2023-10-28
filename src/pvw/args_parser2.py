from pvw.env import EnvironmentManager
from pvw.config import config

import fire

_env_manager = EnvironmentManager()


class Config(object):
    """get or set variables in config"""

    def set(self, name, value):
        """
        set config options.
        Args:
            name (str): The config option, including `venv_path` and `default_env`.
            value (int): The value to the option.
        """
        if name == "venv_path":
            config.set(name, value)

    def get(self, name):
        """
        get config options.
        Args:
            name (str): The config option, including `venv_path` and `default_env`.
        """
        if name == "venv_path":
            path = config.get(name)
            print(path)


class Parser(object):
    """A lightweight Python Venv Wrapper for environment management."""

    def __init__(self) -> None:
        self.config = Config()

    def config(self):
        get_output = self.config.get()
        set_output = self.config.set()
        return [get_output, set_output]

    def ls(self, show_size=False):
        """
        list all venvs.

        Args:
            show_size: whether show sizes of each venv, this operation could take a while.
        """
        if show_size:
            _env_manager.read_size()
        _env_manager.show()

    def create(self, name):
        """
        create a new venv

        Args:
            name: name of venv to create.
        """
        _env_manager.create(name=name)

    def rm(self, *names):
        """
        remove an exists venv

        Args:
            name: name of venv to remove.
        """
        _env_manager.remove(names=names)
        # _env_manager.remove(name=name)

    def activate(self, name):
        """
        activate a venv, using `source pvw actvate env` or `source pvw env`

        Args:
            name: name of venv to activate.
        """
        _env_manager.activate(name=name)
        return "activate"

    def mv(self, src, dest):
        """
        move (or rename) venv `src` to `dest`

        Args:
            src: original venv name, which would disappear after moving
            dest: new venv name
        """
        _env_manager.move(source=src, target=dest)

    def cp(self, src, dest):
        """
        copy venv `src` to `dest`

        Args"
            src: original venv name
            dest: new venv name
        """
        _env_manager.copy(source=src, target=dest)


if __name__ == "__main__":
    fire.Fire(Parser, name="pvw")
