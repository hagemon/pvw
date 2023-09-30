import subprocess
from termcolor import colored
import sys
import os
import shutil


class ShellExecutor:
    def __init__(self) -> None:
        self.on_win = sys.platform.startswith("win")
        self.pipe_name = "_envs._cfg"

    @staticmethod
    def run(cmds: [str], shell=False):
        subprocess.run(
            cmds,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            shell=shell,
        )

    # Config
    def _is_vim_installed(self):
        try:
            self.run(["vim", "--version"])
            return True
        except Exception:
            return False

    def edit_file(self, path):
        if self._is_vim_installed():
            subprocess.run(["vim", path])
        else:
            print(colored("Hint: vim is not installed.", "yellow"))
            print(
                """You can install vim, or use `pvw config get` or `pvw config set` directly.
e.g. `pvw config set venv_path=/PATH/TO/PLACE/VENVS`"""
            )

    def check_python_installation(self):
        try:
            self.run(["python", "--version"])
            return True
        except Exception:
            return False
        
    def save_to_pipe(self, msg):
        pass

    # Environments
    def create_env(self, path):
        self.run(f"python -m venv {path}", shell=True)

    def activate_env(self, path):
        if self.on_win:
            script_path = os.path.join(path, "Scripts", "Activate.ps1")
        else:
            script_path = os.path.join(path, "bin", "activate")

        # Use file as a pipe to communicate with parent process.
        with open(self.pipe_name, 'w') as f:
            f.write(script_path)

    def remove_env(self, path):
        shutil.rmtree(path)


