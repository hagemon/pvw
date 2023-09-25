import os
import json
from shell_executor import ShellExecutor


class Config:
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_dir = os.path.join(script_dir, "config")
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        self.config_path = os.path.join(config_dir, "config.json")
        if not os.path.exists(self.config_path):
            config = {"venv_path": "~/pvw"}
            with open(self.config_path, "w") as f:
                json.dump(config, f)
        self.shell = ShellExecutor()

    def edit(self):
        self.shell.edit_file(self.config_path)

    @property
    def venv_path(self):
        try:
            with open(self.config_path) as f:
                config = json.load(f)
                path = config["venv_path"]
                if path.startswith("~/"):
                    path = os.path.join(os.path.expanduser("~"), path[2:])
                return path
        except Exception as e:
            print(e)

    def build_venv_path(self):
        if not os.path.exists(self.venv_path):
            os.makedirs(self.venv_path)
            print(f"create directory for venvs: {self.venv_path}")


config = Config()
