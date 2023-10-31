import os
from termcolor import colored
from datetime import datetime


class Template:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def write(self):
        path = self.path
        name = self.name
        with open(os.path.join(path, "pyproject.toml"), "w") as f:
            f.write(self._content())
        with open(os.path.join(path, "License"), "w") as f:
            f.write(self._mit_license())
        with open(os.path.join(path, "README.md"), "w") as f:
            f.write(self._readme())
        with open(os.path.join(path, "src", name, "cli.py"), "w") as f:
            f.write(self._cli())

    def build(self):
        path = self.path
        name = self.name
        is_exists = os.path.exists(path=path)
        if is_exists:
            raise NameError(colored(f"Directory {path} has already exists", "red"))
        os.makedirs(path)
        os.makedirs(os.path.join(path, "src", name))
        self.write()

    def _content(self):
        name = self.name
        return f"""[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"


[project]
name = "{name}"
authors = [{{ name = "YOUR_NAME", email = "YOUR_EMAIL@ADDRESS.COM" }}]
description = "YOUR DESCRIPTION HERE"
readme = "README.md"
requires-python = ">=3.6"
license = {{ text = "MIT" }}
version = "0.0.1"
keywords = ["SOME_KEYWORDS"]
classifiers = ["Programming Language :: Python :: 3"]
dependencies = ['importlib-metadata; python_version>"3.6"']

[tool.setuptools.packages.find]
where = ["src"]

# Uncomment to export script file in bin
# [tool.setuptools]
# script-files = ['bin/{name}']

[project.urls]
Homepage = "https://github.com/YOUR_NAME/{name}"
Repository = "https://github.com/YOUR_NAME/{name}"
Documentation = "https://github.com/YOUR_NAME/{name}"

# Uncomment to use scripts
# [project.scripts]
# {name} = "{name}.cli:cli"
"""

    @staticmethod
    def _mit_license():
        return f"""MIT License

Copyright (c) [{datetime.now().year}] [YOUR_NAME]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

    def _readme(self):
        return f"""# {self.name}

Hello, {self.name}.
"""

    def _cli(self):
        return f"""def cli():
    print("Hello, {self.name}")

if __name__ == "__main__":
    cli()
"""
