# pvw

A lightweight (~10kB) python venv wrapper for virtual environment management.

Create venv or standard project in simple command line tool.

Based on the built-in venv since python 3.6.

![](screenshot.png)

## Pre-requirement

- Python >= 3.6
- python-venv

## Installation

```
pip install pvw
```
## Usage

You can either start a raw project with `pvw init`, or just manage virtual envs with **core commands** .

### Start a project

```bash
pvw init PROJ_NAME
```

Initialize a python project, with a simple template as:

```
|- pyproject.toml
|- src
    |- PROJ_NAME
          |- cli.py
|- README.md
|- License
```

You can decide whether creating a specific env for this project.

### Configuration

Get or set the directory `venv_path` where venvs are stored in default.

```bash
pvw config get venv_path # get venv_path variable
pvw config set venv_path=PATH/TO/VENV # set venv_path
```

### Core commands

We use `base` as a demo

#### Show

```shell
# show name, path, and size(optional) of existing venvs.
> pvw ls [--show-size]

Name   Path                  Size
--------------------------------------
env1   C:\Users\venvs\env1   199.42MB
env2   C:\Users\venvs\env2   21.83MB
st     C:\Users\venvs\st     313.99MB
v2     C:\Users\venvs\v2     21.86MB
v3     C:\Users\venvs\v3     21.85MB
```

#### Create
```bash
# Create venv `base` in either way:
pvw create base  # in default venv path
pvw create ./base  # in current directory
pvw create /home/venvs/base  # in specific directory
```

#### Activate/deactivate
```powershell
# For Windows
pvw activate base  # standard way
pvw base  # or a shorter way

deactivate  # exit
```

```shell
# For Linux/MacOS
source pvw activate base  # standard way
source pvw base  # or a shorter way

deactivate # exit
```

#### Copy or move

```shell
# copy or rename from a existing venv
pvw cp base dev  # copy `base` to a new venv `dev`
pvw mv dev foo  # rename `dev` to a new venv `foo`
```

#### Remove

```shell
# remove both `dev` and `foo`
pvw rm dev foo
```

## Build From Source

### Using Makefile

```bash
cd src/pvw
make
sudo make install
```
The executable binary `pvw` and `pvw_py` will be installed in your /usr/bin/ directory.

Note that `pyinstaller` and `termcolor` will also be installed.

### Using setuptools

```bash
pip install --upgrade build setuptools # skip if already installed
python -m build
pip install dist/pvw-x.x.x.tar.gz # x.x.x is the built version of pvw
```

## To-do list

- Simplify activate command in Linux/Mac OS
- Enable setting default venv in terminal
- Add unit tests
- Support specific python version (if installed)