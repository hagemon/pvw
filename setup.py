from setuptools import setup, find_packages
import sys

if sys.platform.startswith("win"):
    shell_file = "pvw.ps1"
else:
    shell_file = "pvw"

setup(
    name="pvw",
    version="0.0.1",
    packages=["pvw"],
    package_dir={
        "pvw": "pvw"
    },
    install_requires=['importlib-metadata; python_version >= "3.6"', "termcolor"],
    entry_points={"console_scripts": ["pvw-py = pvw.main:main"]},
    scripts=[f"bin/{shell_file}"]
)
