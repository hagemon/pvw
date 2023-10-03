# pvw

A lightweight python venv wrapper for virtual environment management.

Based on the built-in venv since python 3.6.

## Installation

### MacOS 

### Linux

### Windows

As we have not gained a proper way to sign my application (which may be improved soon), we provide `.zip` file for Windows users.

1. Download `pvw_win.zip` in [releases](https://github.com/hagemon/pvw/releases) page.
2. Unzip it into a path, e.g. `D:\pvw`.
3. Add the path `D:\pvw` to environment variable `PATH`.

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
pvw create env_name
```

#### Activate venv

Activate an existing venv:

```
pvw activate st
```

To deactivate current venv, just type `deactivate` inside environment. E.g. in Windows

```
(st) PS D:\Users> deactivate
```

Use `python`, `pip` or any other tools inside environment as usual as in `venv`.


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

### Build python executable file

Using `pyinstaller` and `upx` to build a executable file, if you have not installed pyinstaller and upx, try

```bash
pip install pyinstaller
```

#### For Windows

Download [upx](https://upx.github.io/) and decompress it into the path you want, e.g. `D:/upx`.

Finally, build the executable file for python script:

```bash
pyinstaller --onefile --upx-dir=D:/upx main.py --distpath ./dist/win -n pvw_py
```

#### For MacOS / Linux

use `apt` or `homebrew` to install `upx`, then `pyinstaller` should automatically detect the path of `upx`

```bash
pyinstaller --onefile main.py --distpath ./dist/macOS -n pvw_py
```

Hint: the name `pvw_py` should not be modified, or you can custom this name by also editing the `pvw.ps1` script.

### Build shell executable file

#### For Windows

Use [ps2exe](https://github.com/MScholtes/PS2EXE) to build `pvw.ps1` to `pvw.exe`

```powershell
mkdir -ErrorAction Ignore .\dist\win
ps2exe .\pvw.ps1 .\dist\win\pvw.exe
```
Note that `ps2exe` should be ran in powershell 5, then used in powershell core (powershell 7).

#### For MacOS

Use `shc` to build `pvw.sh` to `pvw`

```bash
mkdir -p dist/macOS ; shc -f pvw.sh -o ./dist/macOS/pvw
```

### Add pvw to environment variable (Windows)

Move `pvw.exe` and `pvw_py.exe` into the pvw path, e.g. `D:/pvw`

add `D:/pvw` to environment variable `PATH`


## Architecture

To Be Continued...