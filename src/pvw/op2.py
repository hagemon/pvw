from pvw.config import config
from pvw.env import EnvironmentManager


class Operation:
    """
    Parse args from command line, and feed them into EnvironmentManager to manage venv information.
    """
    def __init__(self) -> None:
        self.env_manager = EnvironmentManager()

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
    @venv_checker
    def create(self):
        name = self.args.name
        self.env_manager.create(name)

    @venv_checker
    def remove(self):
        name = self.args.name
        self.env_manager.remove(name)

    @venv_checker
    def copy(self):
        source = self.args.source
        target = self.args.target
        self.env_manager.copy(source=source, target=target)

    # @venv_checker
    def move(self):
        source = self.args.source
        target = self.args.target
        self.env_manager.move(source=source, target=target)

    @venv_checker
    def show(self, show_size):
        self.env_manager.parse_size = show_size
        self.env_manager.show()

    @venv_checker
    def activate(self):
        self.env_manager.activate(self.args.name)

    # Config Operation
    @venv_checker
    def config(self):
        if self.args.config_command == "set":
            params = self.args.params[0]
            sep = params.index("=")
            key, value = params[:sep], params[sep + 1 :]
            if key == "venv_path":
                config.set(key, value)
                print(config.config)
        elif self.args.config_command == "get":
            key = self.args.key
            if key == "venv_path":
                path = config.get(key)
                print(path)

    def check_python_validation(self):
        return self.env_manager.check_python_installation()
