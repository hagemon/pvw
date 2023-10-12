from setuptools import setup
import sys

if sys.platform.startswith("win"):
    shell_file = "pvw.ps1"
else:
    shell_file = "pvw"

setup(
    name="pvw",
    version="0.0.1",
    readme="README.md",
    requires_python="3.6",
    packages=["pvw"],
    author="hagemon",
    author_email="ooonefolder@gmail.com",
    keywords="venv",
    description="a lightweight python venv wrapper to manage venvs",
    license="MIT",
    package_dir={
        "pvw": "pvw"
    },
    install_requires=['importlib-metadata; python_version >= "3.6"', "termcolor"],
    entry_points={"console_scripts": ["pvw-py = pvw.main:main"]},
    scripts=[f"bin/{shell_file}"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    url="https://github.com/hagemon/pvw"
)
