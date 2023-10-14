# pvw

A lightweight python venv wrapper for virtual environment management.

Based on the built-in venv since python 3.6.

## Pre-requirement

- Python >= 3.6
- python-venv

## Installation

```
pip install pvw
```
## Usage

```
pvw [-h] {ls,config,activate,create,rm,mv,cp}

Manage python venv environments

positional arguments:
  {ls,config,activate,create,rm,mv,cp}
    ls                  List all venvs.
    config              Get or set pvw config.
    activate            Activate venv.
    create              Create a new venv.
    rm                  Remove a venv.
    mv                  Move(rename) venv to another place.
    cp                  Copy venv.
```

You will be asked to set a `venv_path` to store venvs at the first time you use `pvw`.

#### List venvs

```
pvw ls [--show-size]
```

List all created venvs, including name, path and size. Note that size will only be displayed when the `--show-size` modifier is used, which would take a few seconds.

```
Name   Path                  Size
--------------------------------------
env1   C:\Users\venvs\env1   199.42MB
env2   C:\Users\venvs\env2   21.83MB
st     C:\Users\venvs\st     313.99MB
v2     C:\Users\venvs\v2     21.86MB
v3     C:\Users\venvs\v3     21.85MB
```

#### Get or set configs

Get or set the directory `venv_path` where venvs are stored.

```bash
pvw config get venv_path # get venv_path variable
pvw config set venv_path=PATH/TO/VENV # set venv_path
```

#### Create venv

```
pvw create ENV_NAME
```

#### Activate venv

For **Windows**, activate an existing venv with:

```
pvw activate ENV_NAME
```

For **Linux/Mac**, activate venv with `source` command:

```
source pvw activate 
```

or simply use a shorter command

```
source pvw ENV_NAME
```

if your environment name is not conflict with our keywords.

To deactivate current venv, just type `deactivate` inside environment. E.g. in Windows

```
(ENV_NAME) PS D:\Users> deactivate
```

Use `python`, `pip` or any other commands inside environment as usual as in `venv`.


#### Remove venv

```
pvw rm env_name
```

You may be asked to confirm the venv to be removed.

#### Move or rename venv

Move `env1` to a venv `env2`, the original venv would disappear.

```
pvw mv env1 env2
```

You may be asked to confirm the venv to be moved.

#### Copy venv

Copy `env1` to a new venv `env2`

```
pvw cp env1 env2
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


## Architecture

To Be Continued...