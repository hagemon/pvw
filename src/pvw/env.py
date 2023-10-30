from pvw.config import config
import os
from pvw.shell_executor import ShellExecutor
from termcolor import colored


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
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.size = ""  # lazy load

    def set_size(self, size):
        self.size = size

    def to_list(self):
        if self.size:
            return [self.name, self.path, self.size]
        return [self.name, self.path]


class EnvironmentManager:
    """
    Manage and log the principle information about environment, feed then to ShellExecutor to communicate with system.
    """

    def __init__(self):
        self.shell = ShellExecutor()
        self._envs = self.load()
        self.show_size = False

    def load(self):
        config.build_venv_path()
        envs = {}
        venv_info = config.get("venvs")
        for info in venv_info:
            name = info["name"]
            path = info["path"]
            env = Environment(name, path)
            envs[name] = env
        return envs

    def read_size(self):
        self.show_size = True
        for name in self._envs:
            path = os.path.join(config.venv_path, name)
            size = "{:.2f}MB".format(_get_directory_size(path=path))
            self._envs[name].size = size

    # Operations to show or check envs

    def show(self, envs=[]):
        if self.show_size:
            header = ["Name", "Path", "Size"]
        else:
            header = ["Name", "Path"]
        if envs:
            env_list = [self._envs[env].to_list() for env in envs if self.exists(env)]
        else:
            env_list = [self._envs[name].to_list() for name in self._envs]
        col_widths = [
            max(len(str(x)) + 2 for x in col) for col in zip(header, *env_list)
        ]
        print()
        for i, column in enumerate(header):
            print(f"{column:<{col_widths[i]}}", end=" ")
        print()
        print(colored("-" * sum(col_widths), "green"))
        if env_list:
            for row in env_list:
                for i, cell in enumerate(row):
                    print(f"{cell:<{col_widths[i]}}", end=" ")
                print()
        else:
            print("None")
        print()

    def check_python_installation(self):
        return self.shell.check_python_installation()

    def exists(self, name):
        return name in self._envs

    def check_not_exists(self, name):
        if self.exists(name):
            raise NameError(f"Environment named `{name}` has already exists.")

    def check_exists(self, name):
        if not self.exists(name):
            raise NameError(f"Environment `{name}` does not exists.")

    @staticmethod
    def norm_path(path):
        path = os.path.normpath(path)
        name = os.path.basename(path)
        if name == path:  # just type a name   NO!!!! ./name
            return os.path.join(config.venv_path, name), name
        if os.path.isabs(path):
            return path, name
        return os.path.join(os.getcwd(), path), name

    # Operations to modify envs

    def create(self, name):
        path, name = self.norm_path(name)
        self.check_not_exists(name)
        print(f"creating {name} in {path}...")
        self.shell.create_env(path)
        config.add_venv(name, path)
        print(f"{name} created successfully.")

    def activate(self, name):
        self.check_exists(name)
        path = os.path.join(config.venv_path, name)
        self.shell.activate_env(path)

    def remove(self, names):
        valid_names = []
        for name in names:
            try:
                self.check_exists(name)
                valid_names.append(name)
            except NameError as e:
                print(colored(e, "yellow"))
        if not valid_names:
            return
        self.show(envs=valid_names)
        confirm = input(
            colored(f"Sure to remove `{','.join(valid_names)}`? (Y/N)", "red")
        )
        if confirm.lower() == "y":
            for name in valid_names:
                env = self._envs[name]
                path = env.path
                self.shell.remove_env(path)

    def copy(self, source, target):
        self.check_exists(source)
        self.check_not_exists(target)
        print("Start copying...")
        source_path = self._envs[source].path
        target_path = source_path.replace(source, target)
        self.shell.copy_env(source_path, target_path)
        print(
            colored(
                f"venv `{target}` has been successfully copied from `{source}`", "green"
            )
        )

    def move(self, source, target):
        self.check_exists(source)
        self.check_not_exists(target)
        self.show(envs=[source])
        confirm = input(f"Sure to move venv `{source}` to `{target}`? (Y/N)")
        if confirm.lower() == "y":
            print("Start moving...")
            source_path = self._envs[source].path
            target_path = source_path.replace(source, target)
            self.shell.copy_env(source_path, target_path)
            self.shell.remove_env(source_path)
            print(
                colored(
                    f"venv `{target}` has been successfully moved from `{source}`",
                    "green",
                )
            )
