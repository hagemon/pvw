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
        self._envs = self.load_envs()
        self.shell = ShellExecutor()

    @staticmethod
    def load_envs():
        config.build_venv_path()
        envs = []
        for env_name in os.listdir(config.venv_path):
            if env_name.startswith("."):
                continue
            path = os.path.join(config.venv_path, env_name)
            size = "{:.2f}MB".format(_get_directory_size(path=path))
            env = Environment(env_name, path, size)
            envs.append(env)
        return envs

    def print_envs(self):
        header = ["Name", "Path", "Size"]
        env_list = [e.to_list() for e in self._envs]
        col_widths = [max(len(str(x)) for x in col) for col in zip(header, *env_list)]
        for i, column in enumerate(header):
            print(colored(f"{column:<{col_widths[i]}}", "green"), end=" ")
        print()
        for row in env_list:
            for i, cell in enumerate(row):
                print(f"{cell:<{col_widths[i]}}", end=" ")
            print()

    def check_python_version(self):
        return self.shell.check_python_version()

    def check_duplicate(self, name):
        return name in [e.name for e in self._envs]

    def create_environment(self, name):
        if self.check_duplicate(name):
            raise NameError(f"Environment named {name} has already exists.")
        self.shell.create_env(name, config.venv_path)
        print(colored(f"{name} created successfully.", "green"))
