import subprocess
import sys
import os


class ShellExecutor:
    def __init__(self) -> None:
        self.on_win = sys.platform.startswith("win")
        self.py = self.check_python_version()

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
            print("Hint: vim is not installed.")
            print(
                """You can install vim, or use `pvw config get` or `pvw config set` directly.
e.g. `pvw config set venv_path=/PATH/TO/PLACE/VENVS`"""
            )

    def check_python_version(self):
        try:
            self.run(["python", "--version"])
            return "python"
        except Exception:
            try:
                self.run(["python3", "--version"])
                return "python3"
            except Exception:
                raise NameError("python or python3 is not detected.")

    # Environments
    def create_env(self, path):
        self.run(f"{self.py} -m venv {path}", shell=True)

    def activate_env(self, path):
        if self.on_win:
            script_path = os.path.join(path, "Scripts", "Activate.ps1")
            print(script_path)
            p = subprocess.Popen(script_path, stdout=sys.stdout)
        else:
            script_path = os.path.join(path, "bin", "activate")
            print(script_path)
            # self.run(f"source {script_path}", shell=True)
            # subprocess.Popen(f"source {script_path}", shell=True)
            self.run(["./activate_xnix.sh", script_path], shell=True)
