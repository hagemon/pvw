import subprocess
from termcolor import colored


class ShellExecutor:
    def __init__(self) -> None:
        pass

    def hello(self):
        print("hello world")

    def _is_vim_installed(self):
        try:
            subprocess.run(
                ["vim", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
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
            subprocess.run(['python', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return True
        except Exception:
            return False


sh = ShellExecutor()
