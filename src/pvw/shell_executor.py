import subprocess
import sys
import os
import shutil


class ShellExecutor:
    def __init__(self) -> None:
        self.on_win = sys.platform.startswith("win")
        self.py = self.check_python_installation()
        self.pipe_name = os.path.join(os.path.expanduser("~"), ".pvw", "_envs._cfg")

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

    def check_python_installation(self):
        try:
            self.run(["python", "--version"])
            return "python"
        except Exception:
            try:
                self.run(["python3", "--version"])
                return "python3"
            except Exception:
                raise NameError("python or python3 is not detected.")

    def save_to_pipe(self, msg):
        pass

    # Environments
    def create_env(self, path):
        self.run(f"{self.py} -m venv {path}", shell=True)

    def activate_env(self, path):
        if self.on_win:
            script_path = os.path.join(path, "Scripts", "Activate.ps1")
        else:
            script_path = os.path.join(path, "bin", "activate")
        # Use file as a pipe to communicate with parent process.
        with open(self.pipe_name, "w") as f:
            f.write(script_path)

    def remove_env(self, path):
        shutil.rmtree(path)

    def replace_path(self, file_rel_path, source_path, target_path):
        content = ""
        source_prompt = f"({os.path.basename(source_path)})"
        target_prompt = f"({os.path.basename(target_path)})"
        with open(os.path.join(source_path, file_rel_path), "r") as f:
            content = (
                f.read()
                .replace(source_path, target_path)
                .replace(source_prompt, target_prompt)
            )
            with open(os.path.join(target_path, file_rel_path), "w") as f:
                f.write(content)

    def copy_env(self, source_path, target_path):
        self.create_env(target_path)
        if self.on_win:
            script_path = "Scripts"
            shutil.copytree(
                source_path,
                target_path,
                ignore=shutil.ignore_patterns("python*.exe", "pip*.exe"),
                dirs_exist_ok=True,
            )
        else:
            script_path = "bin"
            shutil.copytree(
                source_path,
                target_path,
                ignore=shutil.ignore_patterns(script_path),
                dirs_exist_ok=True,
            )
            shutil.copytree(
                os.path.join(source_path, script_path),
                os.path.join(target_path, script_path),
                ignore=shutil.ignore_patterns("python*", "pip*"),
                dirs_exist_ok=True,
            )

        self.replace_path("pyvenv.cfg", source_path, target_path)
        self.replace_path(
            os.path.join(script_path, "activate"), source_path, target_path
        )
        if self.on_win:
            self.replace_path(
                os.path.join(script_path, "activate.bat"), source_path, target_path
            )
