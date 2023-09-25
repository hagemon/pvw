from config import config
from env import EnvironmentManager


class Operation:
    def __init__(self, args) -> None:
        self.args = args
        self.env_manager = EnvironmentManager()

    # Wrapper
    def args_checker(func):
        def wrapper_func(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Args Checker Error: {e}")

        return wrapper_func

    def venv_checker(func):
        def wrapper_func(*args, **kwargs):
            try:
                config.build_venv_path()
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Venv Checker Error: {e}")

        return wrapper_func

    # Environment operation
    @args_checker
    @venv_checker
    def create(self):
        name = self.args.name
        self.env_manager.create_environment(name)

    @args_checker
    @venv_checker
    def remove(self):
        if self.args.force:
            print(f"Removing item {self.args.name} (forced)")
        else:
            print(f"Removing item {self.args.name}")

    @args_checker
    @venv_checker
    def relocate(self):
        if self.args.dest:
            print(f"Relocating item {self.args.name} to {self.args.dest}")

    @args_checker
    @venv_checker
    def list(self):
        self.env_manager.print_envs()

    @args_checker
    @venv_checker
    def activate(self):
        self.env_manager.activate_environment(self.args.name)

    @args_checker
    @venv_checker
    def deactivate(self):
        print(f"deactivate venv {self.args.name}")

    # Config Operation
    @args_checker
    def config(self):
        if self.args.config_command == "set":
            pass
        elif self.args.config_command == "get":
            pass
        else:  # empty
            config.edit()
        print("config finished")

    @args_checker
    def check_python_validation(self):
        return self.env_manager.check_python_version()
