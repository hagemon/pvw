from config import config
import os
from termcolor import colored
from shell_executor import ShellExecutor


def _get_directory_size(path="."):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size / (1024 * 1024)


class Environment:
    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = size

    def to_list(self):
        return [self.name, self.path, self.size]


class EnvironmentManager:
    def __init__(self):
        self._envs = self.load()
        self.shell = ShellExecutor()

    @staticmethod
    def load():
        config.build_venv_path()
        envs = {}
        for env_name in os.listdir(config.venv_path):
            if env_name.startswith("."):
                continue
            path = os.path.join(config.venv_path, env_name)
            size = "{:.2f}MB".format(_get_directory_size(path=path))
            env = Environment(env_name, path, size)
            envs[env_name] = env
        return envs

    # Operations to show or check envs

    def show(self, env=""):
        header = ["Name", "Path", "Size"]
        if env and self.exists(env):
            env_list = [self._envs[env].to_list()]
        else:
            env_list = [self._envs[name].to_list() for name in self._envs]
        col_widths = [
            max(len(str(x)) + 2 for x in col) for col in zip(header, *env_list)
        ]
        for i, column in enumerate(header):
            print(colored(f"{column:<{col_widths[i]}}", "green"), end=" ")
        print()
        if env_list:
            for row in env_list:
                for i, cell in enumerate(row):
                    print(f"{cell:<{col_widths[i]}}", end=" ")
                print()
        else:
            print("None")

    def check_python_installation(self):
        return self.shell.check_python_installation()

    def exists(self, name):
        return name in self._envs

    # Operations to modify envs

    def create(self, name):
        if self.exists(name):
            raise NameError(f"Environment named {name} has already exists.")
        path = os.path.join(config.venv_path, name)
        print(f"creating {name} in {path}...")
        self.shell.create_env(path)
        print(colored(f"{name} created successfully.", "green"))

    def activate(self, name):
        if not self.exists(name):
            raise NameError(f"No environment named {name}")
        path = os.path.join(config.venv_path, name)
        self.shell.activate_env(path)

    def remove(self, name):
        if not self.exists(name):
            raise NameError(f"Environment {name} does not exists.")
        env = self._envs[name]
        path = env.path
        self.show(env=name)
        confirm = input(colored(f"Sure to remove {name}? (Y/N)", "red"))
        if confirm.lower() == "y":
            self.shell.remove_env(path)

    def copy(self, source, target):
        pass

    def move(self, source, target):
        pass
