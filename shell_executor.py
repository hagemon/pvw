import subprocess
from termcolor import colored


class ShellExecutor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def run(cmds: [str], shell=False):
        subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=shell)

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

    def check_python_version(self):
        try:
            self.run(["python", "--version"])
            return True
        except Exception:
            return False
        

    # Environments
    def create_env(self, name, path):
        try:
            self.run(f'cd {path} && python -m venv {name}', shell=True)
        except Exception as e:
            print(e)
