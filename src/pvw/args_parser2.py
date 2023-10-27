from pvw.op2 import Operation
from pvw.env import EnvironmentManager
import fire

_em = EnvironmentManager()

class Config(object):
    """get or set variables in config"""

    def set(self, name, value):
        """
        set config options.
        Args:
            name (str): The config option, including `venv_path` and `default_env`.
            value (int): The value to the option.
        """
        return f"set {name}"

    def get(self, name):
        """
        get config options.
        Args:
            name (str): The config option, including `venv_path` and `default_env`.
        """
        return f"get {name}"


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
        _em.parse_size = show_size
        _em.show()

    def create(self, name):
        """
        create a new venv

        Args:
            name: name of venv to create.
        """
        return "create"

    def rm(self, name):
        """
        remove an exists venv

        Args:
            name: name of venv to remove.
        """
        return "remove"

    def activate(self, name):
        """
        activate a venv, using `source pvw actvate env` or `source pvw env`

        Args:
            name: name of venv to activate.
        """
        return "activate"

    def mv(self, src, dest):
        """
        move (or rename) venv `src` to `dest`

        Args:
            src: original venv name, which would disappear after moving
            dest: new venv name
        """
        return "move"

    def cp(self, src, dest):
        """
        copy venv `src` to `dest`

        Args"
            src: original venv name
            dest: new venv name
        """
        return "copy"


if __name__ == "__main__":
    fire.Fire(Parser, name="pvw")
