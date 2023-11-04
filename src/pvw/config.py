import os
import json
from pvw.shell_executor import ShellExecutor


class Config:
    def __init__(self):
        user_path = os.path.expanduser("~")
        config_dir = os.path.join(user_path, ".pvw", "config")
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        self.config_path = os.path.join(config_dir, "config.json")
        if not os.path.exists(self.config_path):
            path = self.ask_for_init()
            self.config = {"venv_path": path}
            try:
                self.save()
                print(f"Create config file in {self.config_path}")
            except Exception as e:
                raise NameError(f"invalid venv path {path}.")
        else:
            with open(self.config_path, "r") as f:
                self.config = json.load(f)
        self.check_venv_path()
        self.shell = ShellExecutor()

    def edit(self):
        self.shell.edit_file(self.config_path)

    def get(self, key):
        try:
            return self.config[key]
        except KeyError:
            print(f"No config option named {key}")

    def set(self, key, value):
        if key in self.config:
            self.config[key] = value
            self.save()

    def add_venv(self, name, path):
        self.config["venvs"].append(
            {
                "name": name,
                "path": path,
            }
        )
        self.save()

    def remove_venv(self, names):
        venvs = [info for info in self.config["venvs"] if info["name"] not in names]
        self.config["venvs"] = venvs
        self.save()        

    def check_venv_path(self):
        try:
            if "venvs" not in self.config:
                self.config["venvs"] = []
                path = self.config["venv_path"]
                for env in os.listdir(path):
                    if env.startswith("."):
                        continue
                    self.config["venvs"].append(
                        {
                            "name": env,
                            "path": os.path.join(path, env),
                        }
                    )
                self.save()
            else:
                venvs = self.config["venvs"]
                updated_venvs = [env for env in venvs if os.path.exists(env["path"])]
                if len(venvs) != len(updated_venvs):
                    self.config["venvs"] = updated_venvs
                    self.save()

        except Exception as e:
            print(e)

    def save(self):
        with open(self.config_path, "w") as f:
            json.dump(self.config, f)

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

    def ask_for_init(self):
        path = input("Set the directory for venv (~/venvs):")
        if not path:
            path = "~/venvs"
        if path.startswith("~/"):
            path = os.path.join(os.path.expanduser("~"), path[2:])
        return path


try:
    config = Config()
except Exception:
    raise InterruptedError("Config initialized interrupted.")
