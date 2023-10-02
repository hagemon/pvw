# pvw

A lightweight python venv wrapper for virtual environment management.

Based on the built-in venv since python 3.6.

## Installation

### Windows

### MacOS / Linux

## Usage

### Add environment variable

For Windows, you may firstly add the directory to PATH.

## Build From Source

### Windows

####  Build python executable file

Using `pyinstaller` and `upx` to build a executable file, if you have not installed pyinstaller and upx, try

```bash
pip install pyinstaller
```

then download [upx](https://upx.github.io/) and decompress it into the path you want, e.g. `D:/upx`.

Finally, build the executable file for python script:

```bash
pyinstaller --onefile --upx-dir=D:/upx main.py --distpath . -n pvw_py
```

#### Build powershell executable file

#### Add pvw to environment variable

### MacOS / Linux

## Architecture

To Be Continued...